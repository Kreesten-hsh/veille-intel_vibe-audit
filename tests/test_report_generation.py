"""Tests de validation de la génération dynamique de rapport Jinja2 (templates/vibe-audit/rapport.html.j2).

Vérifie :
1. Le rendu Jinja2 sans erreur à partir des données de leadflow-sandbox.
2. Le dimensionnement dynamique du nombre de pages (ex: 5 pages pour 3 constats + roadmap).
3. L'architecture hybride conforme (Page 1 sombre #0A0F20, Pages 2+ claires #F4F7FB).
4. La présence du bandeau de sévérité ne comptabilisant que les vulnérabilités réelles.
5. La carte séparée des contrôles sains.
6. La présence des preuves reproductibles (Content-Range, horodatage, etc.).
7. Le protocole de re-contrôle J+14 sur la page finale.
"""

import json
from pathlib import Path
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import pytest

TEMPLATE_DIR = Path("templates/vibe-audit")
DATA_PATH = Path("fixtures/leadflow-sandbox/audit-data.json")


@pytest.fixture(scope="module")
def rendered_soup():
    assert DATA_PATH.exists()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=True)
    template = env.get_template("rapport.html.j2")
    html_content = template.render(**data)
    return BeautifulSoup(html_content, "html.parser"), data


def test_dynamic_page_count(rendered_soup):
    """Vérifie que le nombre de pages générées correspond exactement aux données (5 pages attendues)."""
    soup, data = rendered_soup
    pages = soup.find_all("div", class_="page")
    expected_pages = 1 + len(data["findings"]) + (1 if data.get("roadmap") else 0)
    assert len(pages) == expected_pages, f"Le rapport doit compter exactement {expected_pages} pages"
    assert len(pages) == 5, "Le jeu de test de LeadFlow doit produire exactement 5 pages"


def test_hybrid_theme_pages(rendered_soup):
    """Vérifie l'alternance hybride : Page 1 sombre et toutes les pages suivantes claires."""
    soup, _ = rendered_soup
    pages = soup.find_all("div", class_="page")

    # Page 1 : Sombre
    assert "page-dark" in pages[0].get("class", [])
    assert "page-light" not in pages[0].get("class", [])

    # Pages 2 à 5 : Claires
    for i, p in enumerate(pages[1:], start=2):
        assert "page-light" in p.get("class", []), f"La page {i} doit avoir la classe page-light"


def test_stats_banner_isolation(rendered_soup):
    """Vérifie que la barre de sévérité ne compte que les vulnérabilités et isole les contrôles sains."""
    soup, data = rendered_soup
    p1 = soup.find("div", class_="page-dark")
    track = p1.find("div", class_="severity-track")
    assert track is not None

    # Doit contenir les segments des vulnérabilités
    segs = track.find_all("div", class_="seg")
    assert len(segs) == 3  # High, Medium, Low dans ce jeu de données
    for seg in segs:
        assert "seg-safe" not in seg.get("class", [])

    # Carte autonome des contrôles sans anomalie
    safe_badge = p1.find("div", class_="safe-badge-card")
    assert safe_badge is not None
    assert "4 vérifiés conformes" in safe_badge.text


def test_findings_details_and_proofs(rendered_soup):
    """Vérifie la présence des constats, des blocs de preuve et des prompts de remédiation."""
    soup, _ = rendered_soup
    light_pages = soup.find_all("div", class_="page-light")

    # Vérifie que la page du constat SEC-01 contient bien la preuve Content-Range
    sec01_page = None
    for p in light_pages:
        if "SEC-01" in p.text:
            sec01_page = p
            break

    assert sec01_page is not None, "Une page dédiée au constat SEC-01 doit exister"
    assert "Content-Range: 0-1/142" in sec01_page.text
    assert "ALTER TABLE orders ENABLE ROW LEVEL SECURITY;" in sec01_page.text
    assert "142 lignes accessibles publiquement" in sec01_page.text


def test_final_roadmap_and_nda_page(rendered_soup):
    """Vérifie que la dernière page contient bien la feuille de route et le protocole J+14."""
    soup, _ = rendered_soup
    pages = soup.find_all("div", class_="page")
    final_page = pages[-1]

    assert "Feuille de Route" in final_page.text
    assert "Re-Contrôle Gratuit (J+14)" in final_page.text
    assert "Purge sous 30 jours" in final_page.text
    assert "Page 5 / 5" in final_page.text


def test_leadflow_pdf_integrity():
    """Vérifie l'intégrité du fichier PDF exporté output/leadflow-report.pdf."""
    import pypdf
    pdf_path = Path("output/leadflow-report.pdf")
    if pdf_path.exists():
        reader = pypdf.PdfReader(str(pdf_path))
        assert len(reader.pages) == 5, "Le PDF exporté doit compter exactement 5 pages A4 paysage"
        first_page_text = reader.pages[0].extract_text()
        assert "VIBE-AUDIT" in first_page_text
        assert "leadflow-demo.example" in first_page_text

