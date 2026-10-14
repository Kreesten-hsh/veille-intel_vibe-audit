"""Sas de consentement technique bloquant (ADR-04 & FR-010).

Vérifie l'existence, l'intégrité, le signataire et la validité temporelle
du fichier de consentement écrit Markdown (consent/<client_id>.md)
avant d'autoriser la moindre action d'audit ou d'inspection.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Optional
import yaml


class ConsentError(Exception):
    """Exception racine pour toute violation ou anomalie du sas de consentement."""
    pass


class ConsentMissingError(ConsentError):
    """Levée lorsque le fichier de consentement est absent."""
    pass


class ConsentEmptyError(ConsentError):
    """Levée lorsque le fichier de consentement existe mais est vide."""
    pass


class ConsentExpiredError(ConsentError):
    """Levée lorsque la date d'autorisation est dépassée."""
    pass


class ConsentNotStartedError(ConsentError):
    """Levée lorsque la fenêtre temporelle d'autorisation n'a pas encore débuté."""
    pass


class ConsentInvalidSignerError(ConsentError):
    """Levée lorsque le signataire ou son attestation d'autorité est non renseigné."""
    pass


class ConsentTargetMismatchError(ConsentError):
    """Levée lorsque l'URL cible analysée ne correspond pas au périmètre autorisé."""
    pass


class ConsentRevokedError(ConsentError):
    """Levée lorsque le statut du consentement n'est pas VALIDE (ex: REVOQUE)."""
    pass


@dataclass(frozen=True)
class ConsentRecord:
    """Structure immuable représentant un accord de consentement validé."""
    reference: str
    client_id: str
    client_nom: str
    client_email: str
    url_cible: str
    date_debut: datetime
    date_expiration: datetime
    recheck_expiration: Optional[datetime]
    statut: str
    file_path: Path
    body_markdown: str


def _parse_datetime(val: object) -> datetime:
    """Convertit une chaîne ou un objet date en datetime UTC conscient."""
    if isinstance(val, datetime):
        dt = val
    elif isinstance(val, str):
        # Supporte ISO 8601 complet ou simple date YYYY-MM-DD
        cleaned = val.strip()
        if " " in cleaned and "T" not in cleaned:
            cleaned = cleaned.replace(" ", "T")
        dt = datetime.fromisoformat(cleaned)
    else:
        raise ValueError(f"Format de date non convertible : {val}")

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _is_placeholder(val: Optional[str]) -> bool:
    """Détecte si une valeur contient un placeholder modèle non rempli (ex: [NOM...])."""
    if not val:
        return True
    s = val.strip()
    return s.startswith("[") and s.endswith("]")


def verify_consent(
    client_id: str,
    consent_dir: Optional[Path] = None,
    target_url: Optional[str] = None,
    now: Optional[datetime] = None,
) -> ConsentRecord:
    """Vérifie rigoureusement la validité de l'accord de consentement pour un client donné.

    Args:
        client_id: Identifiant unique du client (correspondant à consent/<client_id>.md).
        consent_dir: Répertoire de stockage des consentements (défaut: ./consent).
        target_url: URL cible optionnelle dont on souhaite vérifier l'adéquation avec le mandat.
        now: Horodatage actuel de vérification (défaut: datetime.now(timezone.utc)).

    Returns:
        ConsentRecord: L'accord de consentement validé et typé.

    Raises:
        ConsentMissingError: Si le fichier consent/<client_id>.md n'existe pas.
        ConsentEmptyError: Si le fichier est vide.
        ConsentExpiredError: Si la fenêtre d'intervention est échue.
        ConsentNotStartedError: Si l'autorisation n'a pas encore débuté.
        ConsentInvalidSignerError: Si le signataire est un placeholder ou absent.
        ConsentTargetMismatchError: Si target_url ne correspond pas à l'URL autorisée.
        ConsentRevokedError: Si le statut n'est pas VALIDE.
    """
    if consent_dir is None:
        consent_dir = Path("consent")

    file_path = consent_dir / f"{client_id}.md"

    # 1. Vérification de présence physique
    if not file_path.exists():
        raise ConsentMissingError(
            f"ERREUR : Consentement écrit obligatoire manquant ({file_path})."
        )

    raw_text = file_path.read_text(encoding="utf-8").strip()

    # 2. Vérification de non-vacuité
    if not raw_text:
        raise ConsentEmptyError(
            f"ERREUR : Le fichier de consentement est vide ({file_path})."
        )

    # 3. Extraction du frontmatter YAML
    parts = raw_text.split("---", 2)
    if len(parts) < 3:
        raise ConsentError(
            f"ERREUR : Le fichier de consentement {file_path} ne possède pas d'en-tête YAML valide délimité par '---'."
        )

    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as err:
        raise ConsentError(
            f"ERREUR : En-tête YAML non analysable dans {file_path} : {err}"
        ) from err

    body_md = parts[2].strip()

    # 4. Vérification du statut
    statut = str(data.get("statut", "")).strip().upper()
    if statut != "VALIDE":
        raise ConsentRevokedError(
            f"ERREUR : Le statut du consentement dans {file_path} est '{statut}' (attendu: VALIDE)."
        )

    # 5. Vérification du signataire
    client_nom = data.get("client_nom")
    if not client_nom or _is_placeholder(client_nom):
        raise ConsentInvalidSignerError(
            f"ERREUR : Le signataire (client_nom) est manquant ou contient un modèle non renseigné dans {file_path}."
        )

    # 6. Vérification des dates
    current_time = _parse_datetime(now) if now is not None else datetime.now(timezone.utc)

    try:
        date_debut = _parse_datetime(data.get("date_debut"))
        date_exp = _parse_datetime(data.get("date_expiration"))
    except (ValueError, TypeError) as err:
        raise ConsentError(
            f"ERREUR : Dates d'autorisation invalides ou absentes dans {file_path} : {err}"
        ) from err

    if current_time < date_debut:
        raise ConsentNotStartedError(
            f"ERREUR : L'autorisation n'a pas encore débuté (début prévu: {date_debut.isoformat()})."
        )

    if current_time > date_exp:
        raise ConsentExpiredError(
            "ERREUR : La date d'autorisation est échue."
        )

    # 7. Vérification de re-contrôle (optionnel)
    recheck_exp = None
    if data.get("recheck_expiration") and not _is_placeholder(data.get("recheck_expiration")):
        try:
            recheck_exp = _parse_datetime(data.get("recheck_expiration"))
        except (ValueError, TypeError):
            recheck_exp = None

    # 8. Vérification de l'adéquation du périmètre URL
    auth_url = str(data.get("url_cible", "")).strip()
    if target_url is not None:
        target_clean = target_url.strip().rstrip("/")
        auth_clean = auth_url.rstrip("/")
        if _is_placeholder(auth_url) or (auth_clean and target_clean != auth_clean):
            raise ConsentTargetMismatchError(
                f"ERREUR : L'URL cible '{target_url}' ne correspond pas à l'URL autorisée '{auth_url}'."
            )

    return ConsentRecord(
        reference=str(data.get("reference", "NON_DEFINI")),
        client_id=client_id,
        client_nom=str(client_nom),
        client_email=str(data.get("client_email", "")),
        url_cible=auth_url,
        date_debut=date_debut,
        date_expiration=date_exp,
        recheck_expiration=recheck_exp,
        statut=statut,
        file_path=file_path,
        body_markdown=body_md,
    )


def enforce_consent_or_exit(
    client_id: str,
    consent_dir: Optional[Path] = None,
    target_url: Optional[str] = None,
    now: Optional[datetime] = None,
) -> ConsentRecord:
    """Sas technique bloquant : valide le consentement ou interrompt immédiatement le processus.

    Conforme à ADR-04 et FR-010 : en cas d'erreur ou d'absence, affiche le message d'erreur
    sur stderr et invoque sys.exit(1).
    """
    try:
        return verify_consent(
            client_id=client_id,
            consent_dir=consent_dir,
            target_url=target_url,
            now=now,
        )
    except ConsentError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
