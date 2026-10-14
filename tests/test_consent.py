"""Tests de validation et de conformité légale de l'accord de consentement Vibe-Audit.

Valide les critères requis :
1. Présence et intégrité du fichier templates/vibe-audit/accord-consentement.md.
2. Structure machine-readable (frontmatter YAML) pour l'intégration avec consent_gate.
3. Conformité aux garde-fous (Guardrail #3 : consentement écrit, art. 323-1 Code pénal, RGPD).
4. Clauses de confidentialité bilatérale (NDA), arrêt d'urgence PII et destruction sous 30 jours.
5. Périmètre passif non destructif et exclusion ferme des services tiers (Stripe).
6. Protocole de re-contrôle gratuit inclus à J+14.
7. Format clair prêt à signer ou valider par écrit.
"""

from pathlib import Path
import yaml
import pytest

TEMPLATE_PATH = Path("templates/vibe-audit/accord-consentement.md")


@pytest.fixture
def consent_doc():
    assert TEMPLATE_PATH.exists(), f"Le template d'accord {TEMPLATE_PATH} doit exister"
    raw = TEMPLATE_PATH.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    assert len(parts) >= 3, "Le document doit contenir un frontmatter YAML délimité par '---'"
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]
    return frontmatter, body


def test_frontmatter_fields(consent_doc):
    """Vérifie la présence des champs obligatoires dans le frontmatter YAML."""
    fm, _ = consent_doc
    required_keys = [
        "reference",
        "client_nom",
        "client_qualite",
        "societe_projet",
        "client_email",
        "auditeur_nom",
        "auditeur_qualite",
        "url_cible",
        "repo_ou_archive",
        "date_debut",
        "date_expiration",
        "recheck_expiration",
        "statut",
    ]
    for key in required_keys:
        assert key in fm, f"Le champ '{key}' doit être présent dans le frontmatter"

    assert fm["auditeur_nom"] == "Kreesten Agboton"
    assert "VALIDE" in fm["statut"]


def test_legal_references_and_authority(consent_doc):
    """Vérifie les mentions légales obligatoires (Code pénal, RGPD, attestation d'autorité)."""
    _, body = consent_doc
    assert "323-1" in body, "L'article 323-1 du Code pénal doit être explicitement mentionné"
    assert "RGPD" in body or "Règlement UE 2016/679" in body, "La référence au RGPD doit figurer"
    assert "honneur" in body.lower(), "L'attestation sur l'honneur de propriété doit être stipulée"


def test_scope_and_non_destructive_boundaries(consent_doc):
    """Vérifie le caractère strictement passif et les exclusions d'intrusion."""
    _, body = consent_doc
    assert "passif" in body.lower(), "La nature passive de l'évaluation doit être stipulée"
    assert "non destructif" in body.lower() or "non-destructif" in body.lower()
    assert "Stripe" in body, "Les tiers de paiement (Stripe) doivent être mentionnés hors périmètre"
    assert "déni de service" in body.lower() or "dos" in body.lower(), "Le DoS/DDoS doit être interdit"


def test_confidentiality_nda_and_data_destruction(consent_doc):
    """Vérifie les clauses de confidentialité bilatérale (NDA), arrêt PII et purge 30 jours."""
    _, body = consent_doc
    assert "confidentialité" in body.lower()
    assert "entraînement" in body.lower(), "L'interdiction d'entraînement de modèles IA doit être garantie"
    assert "arrêt d'urgence" in body.lower() or "données personnelles" in body.lower(), (
        "La procédure d'arrêt d'urgence en cas de PII doit être présente"
    )
    assert "30 jours" in body, "L'engagement de destruction des données sous 30 jours doit figurer"


def test_recheck_j14_clause(consent_doc):
    """Vérifie l'inclusion explicite du protocole de re-contrôle gratuit à J+14."""
    _, body = consent_doc
    assert "J+14" in body or "14 jours" in body, "La clause de re-contrôle à J+14 doit être formelle"
    assert "gratuit" in body.lower(), "Le re-contrôle doit être stipulé gratuit / inclus"


def test_signature_and_approval_format(consent_doc):
    """Vérifie que le gabarit est prêt à signer avec cases d'engagement et mentions types."""
    _, body = consent_doc
    assert "[ ]" in body, "Des cases à cocher d'engagement doivent être fournies"
    assert "Bon pour mandat" in body, "La mention d'approbation 'Bon pour mandat' doit être présente"
    assert "Kreesten Agboton" in body, "L'auditeur Kreesten Agboton doit être désigné"
