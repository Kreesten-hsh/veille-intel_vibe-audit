"""Tests unitaires du sas technique bloquant consent_gate (ADR-04 & FR-010).

Vérifie :
1. Arrêt bloquant immédiat (ConsentMissingError / exit 1) si le fichier de consentement est absent.
2. Arrêt bloquant (ConsentEmptyError / exit 1) si le fichier est vide.
3. Arrêt bloquant (ConsentExpiredError / exit 1) si la date d'autorisation est échue.
4. Arrêt bloquant (ConsentInvalidSignerError) si le signataire n'est pas renseigné.
5. Arrêt bloquant (ConsentTargetMismatchError) si l'URL cible ne correspond pas au mandat.
6. Validation réussie (ConsentRecord complet) pour un accord valide et actif.
"""

from datetime import datetime, timezone
from pathlib import Path
import sys
import pytest

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.vibe_audit.consent_gate import (
    ConsentEmptyError,
    ConsentExpiredError,
    ConsentInvalidSignerError,
    ConsentMissingError,
    ConsentNotStartedError,
    ConsentRecord,
    ConsentTargetMismatchError,
    enforce_consent_or_exit,
    verify_consent,
)

FIXTURES_DIR = Path("tests/fixtures/consent")
TEST_NOW = datetime(2026, 10, 13, 14, 0, 0, tzinfo=timezone.utc)


def test_consent_gate_missing():
    """Vérifie le blocage immédiat lorsque le fichier de consentement n'existe pas."""
    with pytest.raises(ConsentMissingError) as exc_info:
        verify_consent(
            client_id="client_inconnu_sans_accord",
            consent_dir=FIXTURES_DIR,
            now=TEST_NOW,
        )
    msg = str(exc_info.value)
    assert "ERREUR : Consentement écrit obligatoire manquant" in msg
    assert "client_inconnu_sans_accord.md" in msg


def test_consent_gate_empty():
    """Vérifie le blocage immédiat sur un fichier de consentement vide (0 octet)."""
    with pytest.raises(ConsentEmptyError) as exc_info:
        verify_consent(
            client_id="consent_empty",
            consent_dir=FIXTURES_DIR,
            now=TEST_NOW,
        )
    msg = str(exc_info.value)
    assert "ERREUR : Le fichier de consentement est vide" in msg


def test_consent_gate_expired():
    """Vérifie le blocage immédiat lorsque la date d'autorisation est échue."""
    with pytest.raises(ConsentExpiredError) as exc_info:
        verify_consent(
            client_id="consent_expired",
            consent_dir=FIXTURES_DIR,
            now=TEST_NOW,
        )
    assert "ERREUR : La date d'autorisation est échue." in str(exc_info.value)


def test_consent_gate_no_signer():
    """Vérifie le blocage lorsque le signataire contient un placeholder non rempli."""
    with pytest.raises(ConsentInvalidSignerError) as exc_info:
        verify_consent(
            client_id="consent_no_signer",
            consent_dir=FIXTURES_DIR,
            now=TEST_NOW,
        )
    assert "ERREUR : Le signataire (client_nom) est manquant" in str(exc_info.value)


def test_consent_gate_not_started():
    """Vérifie le blocage lorsque l'intervention est tentée avant la date de début."""
    too_early = datetime(2026, 10, 1, 0, 0, 0, tzinfo=timezone.utc)
    with pytest.raises(ConsentNotStartedError) as exc_info:
        verify_consent(
            client_id="consent_ok",
            consent_dir=FIXTURES_DIR,
            now=too_early,
        )
    assert "ERREUR : L'autorisation n'a pas encore débuté" in str(exc_info.value)


def test_consent_gate_target_url_mismatch():
    """Vérifie le blocage lorsque l'URL analysée ne correspond pas au périmètre autorisé."""
    with pytest.raises(ConsentTargetMismatchError) as exc_info:
        verify_consent(
            client_id="consent_ok",
            consent_dir=FIXTURES_DIR,
            target_url="https://autre-cible-non-autorisee.fr",
            now=TEST_NOW,
        )
    assert "ne correspond pas à l'URL autorisée" in str(exc_info.value)


def test_consent_gate_valid_record():
    """Vérifie la validation complète d'un accord en règle et la conformité du record."""
    record = verify_consent(
        client_id="consent_ok",
        consent_dir=FIXTURES_DIR,
        target_url="https://app.monprojet.com",
        now=TEST_NOW,
    )
    assert isinstance(record, ConsentRecord)
    assert record.client_nom == "Jean Dupont"
    assert record.url_cible == "https://app.monprojet.com"
    assert record.statut == "VALIDE"
    assert record.reference == "VA-CONSENT-20261013-001"
    assert "Accord formel validé" in record.body_markdown


def test_consent_gate_enforce_cli_exit(capsys):
    """Vérifie le sas d'exécution bloquant en CLI qui affiche l'erreur sur stderr et fait exit(1)."""
    with pytest.raises(SystemExit) as exc_info:
        enforce_consent_or_exit(
            client_id="inexistant",
            consent_dir=FIXTURES_DIR,
            now=TEST_NOW,
        )
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERREUR : Consentement écrit obligatoire manquant" in captured.err


def test_consent_gate_leadflow_demo_default_consent():
    """Vérifie que l'accord de la cible de démo LeadFlow dans consent/leadflow-demo.md est valide."""
    root_consent_dir = ROOT_DIR / "consent"
    record = verify_consent(
        client_id="leadflow-demo",
        consent_dir=root_consent_dir,
        target_url="https://leadflow-demo.example",
        now=TEST_NOW,
    )
    assert record.reference == "VA-CONSENT-20261013-DEMO"
    assert record.client_nom == "Kreesten Agboton"
    assert record.statut == "VALIDE"

