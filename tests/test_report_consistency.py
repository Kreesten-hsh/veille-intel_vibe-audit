"""Tests de cohérence automatique du rapport Vibe-Audit (Version Hybride Premium).

Valide les règles d'acceptation du rapport :
1. Approche hybride : Page 1 sombre (#0A0F20) et Page 2 claire (#F4F7FB) avec blocs sombres
2. Cohérence des chiffres (barre empilée = somme des vulnérabilités)
3. Cohérence du périmètre (aucun composant hors périmètre décrit comme sain)
4. Traçabilité des preuves (horodatage UTC, Content-Range, anon key, URL standard d'exemple)
5. Neutralité des statuts (indicateurs neutres pour tests post-correction)
6. Remédiation nuancée (hypothèse documentée)
7. Mention de démonstration compacte et non ambiguë (pastille DÉMO)
8. Exactitude de la référence OWASP (WSTG-ATHZ-02 / BOLA et pas WSTG-CONF-05)
9. Export PDF haute fidélité (exactement 2 pages A4 paysage)
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


def test_hybrid_theme_structure(soup):
    """Vérifie l'approche hybride : page 1 sombre et page 2 claire."""
    pages = soup.find_all("div", class_="page")
    assert len(pages) == 2, "Le prototype doit contenir exactement 2 pages"

    p1 = pages[0]
    p2 = pages[1]

    assert "page-dark" in p1.get("class", []), "La page 1 doit avoir la classe page-dark"
    assert "page-light" in p2.get("class", []), "La page 2 doit avoir la classe page-light"

    style_tag = soup.find("style")
    assert style_tag is not None
    css_content = style_tag.string
    assert "#0A0F20" in css_content, "La page sombre doit utiliser #0A0F20"
    assert "#F4F7FB" in css_content, "La page claire doit utiliser #F4F7FB"


def test_severity_bar_counts_only_vulnerabilities(soup):
    """Vérifie que la barre empilée ne compte QUE les vulnérabilités réelles."""
    bar = soup.find("div", class_="severity-track")
    assert bar is not None

    segments = bar.find_all("div", class_="seg")
    assert len(segments) == 3, "Doit contenir 3 segments de vulnérabilité (élevé, moyen, faible)"

    safe_segs = bar.find_all("div", class_="seg-safe")
    assert len(safe_segs) == 0, "Les contrôles sûrs ne doivent pas être mélangés dans la barre"

    safe_badge = soup.find("div", class_="safe-badge-card")
    assert safe_badge is not None
    assert "4 vérifiés conformes" in safe_badge.get_text()


def test_perimeter_consistency_no_false_claims(soup):
    """Vérifie qu'aucun composant hors périmètre (Stripe) n'est déclaré sain."""
    p1 = soup.find_all("div", class_="page")[0]
    p1_text = p1.get_text()

    assert "Stripe est saine" not in p1_text
    assert "Stripe sont sains" not in p1_text
    assert "n'ont pas été évalués dans cette mission" in p1_text
    assert "Hors périmètre" in p1_text


def test_neutral_validation_indicators(soup):
    """Vérifie que les tests de validation à venir ont des indicateurs neutres."""
    p2 = soup.find_all("div", class_="page")[1]
    validation_card = p2.find("div", class_="validation-card")
    assert validation_card is not None

    todo_indicators = validation_card.find_all("span", class_="bullet-todo")
    assert len(todo_indicators) >= 2, "Les tests non encore exécutés doivent porter un indicateur neutre"


def test_proof_traceability_content_range(soup):
    """Vérifie que la preuve technique contient les critères de traçabilité."""
    p2 = soup.find_all("div", class_="page")[1]
    code_surface = p2.find("div", class_="code-surface")
    assert code_surface is not None

    text = code_surface.get_text()
    assert "Content-Range: 0-1/142" in text
    assert "13/10/2026" in text
    assert "15:30 UTC" in text
    assert "leadflow-demo.example" in text


def test_sql_remediation_hypotheses(soup):
    """Vérifie que le prompt de remédiation documente explicitement ses hypothèses."""
    p2 = soup.find_all("div", class_="page")[1]
    prompt_box = p2.find_all("div", class_="code-surface")[1]
    assert prompt_box is not None

    text = prompt_box.get_text()
    assert "Hypothèse" in text
    assert "user_id" in text
    assert "ENABLE ROW LEVEL SECURITY" in text


def test_owasp_reference_exactness(soup):
    """Vérifie que la méthode OWASP citée est exacte (ATHZ-02 / BOLA et pas CONF-05)."""
    full_text = soup.get_text()
    assert "WSTG-CONF-05" not in full_text
    assert "OWASP WSTG-ATHZ-02" in full_text
    assert "API1:2023" in full_text


def test_demo_pill_compact(soup):
    """Vérifie la présence de la pastille de démonstration compacte."""
    demo_pills = soup.find_all("span", class_="pill-demo")
    assert len(demo_pills) >= 1
    assert "DÉMO" in demo_pills[0].get_text()


def test_pdf_rendering_exact_page_count():
    """Vérifie que le PDF généré existe et contient exactement 2 pages."""
    assert PDF_PATH.exists(), f"Le fichier PDF {PDF_PATH} doit exister"
    reader = pypdf.PdfReader(str(PDF_PATH))
    assert len(reader.pages) == 2, f"Le PDF doit comporter exactement 2 pages, trouvé {len(reader.pages)}"
