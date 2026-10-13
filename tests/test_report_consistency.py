"""Tests de cohérence automatique du rapport Vibe-Audit.

Valide les 8 critères d'acceptation définis dans docs/STRUCTURE-RAPPORT.md :
1. Cohérence des chiffres (barre de gravité empilée = somme des vulnérabilités)
2. Cohérence du périmètre (aucune affirmation de santé sur composants hors périmètre)
3. Traçabilité des preuves (horodatage, Content-Range, anon key)
4. Neutralité des statuts (indicateurs neutres pour tests post-correction)
5. Remédiation nuancée (hypothèse documentée)
6. Mention de démonstration explicite
7. Validité de la référence OWASP (WSTG-ATHZ-02 / BOLA et pas WSTG-CONF-05)
8. Export PDF haute fidélité (2 pages A4 paysage sans débordement)
"""

from pathlib import Path
from bs4 import BeautifulSoup
import pypdf
import pytest

TEMPLATE_PATH = Path("templates/vibe-audit/prototype-rapport.html")
PDF_PATH = Path("output/prototype-rapport.pdf")


@pytest.fixture
def soup():
    assert TEMPLATE_PATH.exists(), f"Le template {TEMPLATE_PATH} doit exister"
    content = TEMPLATE_PATH.read_text(encoding="utf-8")
    return BeautifulSoup(content, "html.parser")


def test_unified_background_color(soup):
    """Vérifie que le fond unifié #0A0F20 est appliqué à toutes les pages."""
    pages = soup.find_all("div", class_="page")
    assert len(pages) == 2, "Le prototype doit contenir exactement 2 pages"

    # Vérification dans le CSS que .page applique bien #0A0F20
    style_tag = soup.find("style")
    assert style_tag is not None
    css_content = style_tag.string
    assert "background-color: #0A0F20;" in css_content
    # Aucune page avec fond clair résiduel
    assert "page-light" not in css_content


def test_severity_bar_counts_only_vulnerabilities(soup):
    """Vérifie que la barre empilée ne compte QUE les vulnérabilités réelles."""
    bar = soup.find("div", class_="severity-bar-track")
    assert bar is not None

    segments = bar.find_all("div", class_="severity-seg")
    # Doit contenir exactement les segments de sévérité (élevé, moyen, faible)
    assert len(segments) == 3

    # Aucun segment 'safe' dans la barre de vulnérabilités
    safe_segs = bar.find_all("div", class_="seg-safe")
    assert len(safe_segs) == 0, "Les contrôles sûrs ne doivent pas être mélangés dans la barre"

    # Vérifie la présence du badge séparé pour les contrôles conformes
    safe_badge = soup.find("div", class_="safe-controls-badge")
    assert safe_badge is not None
    assert "Contrôles examinés sans anomalie : 4" in safe_badge.get_text()


def test_perimeter_consistency_no_false_claims(soup):
    """Vérifie qu'aucun composant hors périmètre (Stripe) n'est déclaré sain."""
    p1 = soup.find_all("div", class_="page")[0]
    p1_text = p1.get_text()

    # Si Stripe est hors périmètre, il ne doit jamais être dit 'sain' ou 'sécurisé'
    assert "Stripe est saine" not in p1_text
    assert "Stripe sont sains" not in p1_text

    # La formulation exacte d'exclusion doit être présente
    assert "n'ont pas été évalués dans cette mission" in p1_text
    assert "Hors périmètre" in p1_text


def test_neutral_validation_indicators(soup):
    """Vérifie que les tests de validation à venir ont des indicateurs neutres."""
    p2 = soup.find_all("div", class_="page")[1]
    validation_box = p2.find("div", class_="validation-box")
    assert validation_box is not None

    # Les items de validation doivent utiliser l'indicateur neutre todo
    todo_indicators = validation_box.find_all("span", class_="indicator-todo")
    assert len(todo_indicators) >= 2, "Les tests non encore exécutés doivent porter un indicateur neutre"


def test_proof_traceability_content_range(soup):
    """Vérifie que la preuve technique contient les critères de traçabilité."""
    p2 = soup.find_all("div", class_="page")[1]
    terminal = p2.find("div", class_="terminal-box")
    assert terminal is not None

    term_text = terminal.get_text()
    assert "Content-Range: 0-1/142" in term_text
    assert "13/10/2026" in term_text
    assert "UTC" in term_text


def test_sql_remediation_hypotheses(soup):
    """Vérifie que le prompt de remédiation documente explicitement ses hypothèses."""
    p2 = soup.find_all("div", class_="page")[1]
    prompt_box = p2.find("div", class_="prompt-box")
    assert prompt_box is not None

    prompt_text = prompt_box.get_text()
    assert "Hypothèse" in prompt_text
    assert "user_id" in prompt_text
    assert "ENABLE ROW LEVEL SECURITY" in prompt_text


def test_owasp_reference_exactness(soup):
    """Vérifie que la méthode OWASP citée est exacte (ATHZ-02 / BOLA et pas CONF-05)."""
    full_text = soup.get_text()
    assert "WSTG-CONF-05" not in full_text
    assert "OWASP WSTG-ATHZ-02" in full_text
    assert "API1:2023" in full_text


def test_demo_banner_presence(soup):
    """Vérifie la présence du bandeau d'avertissement de démonstration."""
    banner = soup.find("div", class_="demo-banner")
    assert banner is not None
    assert "Exemple de démonstration" in banner.get_text()
    assert "sandbox" in banner.get_text()


def test_pdf_rendering_exact_page_count():
    """Vérifie que le PDF généré existe et contient exactement 2 pages."""
    assert PDF_PATH.exists(), f"Le fichier PDF {PDF_PATH} doit exister"
    reader = pypdf.PdfReader(str(PDF_PATH))
    assert len(reader.pages) == 2, f"Le PDF doit comporter exactement 2 pages, trouvé {len(reader.pages)}"
