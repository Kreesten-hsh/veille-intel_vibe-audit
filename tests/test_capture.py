import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
from scripts.capture import extract_text, is_allowed, capture_url, load_targets, save_snapshot_and_diff

HTML_FIXTURE = """
<!DOCTYPE html>
<html>
<head>
    <style>body { font-family: sans-serif; }</style>
    <script>console.log("tracking code");</script>
</head>
<body>
    <nav><a href="/">Accueil</a><a href="/pricing">Tarifs</a></nav>
    <header><h1>Bannière</h1></header>
    <main>
        <h2>Offre SaaS Pro</h2>
        <p>Abonnement à 49 € / mois sans engagement.</p>
    </main>
    <footer><p>&copy; 2026 Entreprise Fictive</p></footer>
</body>
</html>
"""

def test_extract_text_filters_noise():
    text = extract_text(HTML_FIXTURE)
    assert "tracking code" not in text
    assert "font-family" not in text
    assert "Accueil" not in text
    assert "Entreprise Fictive" not in text
    assert "Offre SaaS Pro" in text
    assert "Abonnement à 49 € / mois sans engagement." in text

def test_robots_txt_disallow_respected():
    def mock_handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            content = "User-agent: *\nDisallow: /admin\nDisallow: /private/\n"
            return httpx.Response(200, text=content)
        return httpx.Response(200, text="OK")

    transport = httpx.MockTransport(mock_handler)
    with httpx.Client(transport=transport) as client:
        assert is_allowed("https://example.com/admin", client) is False
        assert is_allowed("https://example.com/private/secret", client) is False
        assert is_allowed("https://example.com/pricing", client) is True

def test_hash_stable():
    text = extract_text(HTML_FIXTURE)
    h1 = hashlib.sha256(text.encode("utf-8")).hexdigest()
    h2 = hashlib.sha256(text.encode("utf-8")).hexdigest()
    assert h1 == h2
    assert len(h1) == 64

def test_capture_url_creates_snapshot_and_index(tmp_path: Path):
    def mock_handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nAllow: /\n")
        if request.url.path == "/pricing":
            return httpx.Response(200, text=HTML_FIXTURE)
        return httpx.Response(404)

    transport = httpx.MockTransport(mock_handler)
    with httpx.Client(transport=transport) as client:
        sha = capture_url("https://example.com/pricing", client, out_dir=tmp_path)
        assert sha is not None

        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        snapshot_file = tmp_path / "example.com" / f"{today}.txt"
        assert snapshot_file.exists()
        assert "Offre SaaS Pro" in snapshot_file.read_text(encoding="utf-8")

        index_file = tmp_path / "index.csv"
        assert index_file.exists()
        lines = index_file.read_text(encoding="utf-8").strip().splitlines()
        assert lines[0] == "url,date,sha256"
        assert f"https://example.com/pricing,{today},{sha}" in lines[1]

def test_load_targets(tmp_path: Path):
    yaml_file = tmp_path / "targets.yaml"
    yaml_file.write_text("targets:\n  - name: Test\n    url: https://example.com/test\n", encoding="utf-8")
    targets = load_targets(yaml_file)
    assert len(targets) == 1
    assert targets[0]["url"] == "https://example.com/test"

def test_save_snapshot_and_diff_evolution(tmp_path: Path):
    url = "https://competitor.example/pricing"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Première capture : pas de N-1, donc pas de diff
    res1 = save_snapshot_and_diff(url, "Offre Starter : 19 €/mois\nOffre Pro : 49 €/mois\n", out_dir=tmp_path)
    assert res1["changed"] is False
    assert res1["diff_path"] is None
    assert (tmp_path / "competitor.example" / "pricing" / f"{today}.txt").exists()

    # Deuxième capture identique : aucun changement
    res2 = save_snapshot_and_diff(url, "Offre Starter : 19 €/mois\nOffre Pro : 49 €/mois\n", out_dir=tmp_path)
    assert res2["changed"] is False
    assert res2["diff_path"] is None

    # Troisième capture avec modification de prix (N vs N-1)
    res3 = save_snapshot_and_diff(url, "Offre Starter : 29 €/mois\nOffre Pro : 59 €/mois\n", out_dir=tmp_path)
    assert res3["changed"] is True
    assert res3["diff_path"] is not None
    diff_file = Path(res3["diff_path"])
    assert diff_file.exists()
    diff_content = diff_file.read_text(encoding="utf-8")
    assert "-Offre Starter : 19 €/mois" in diff_content
    assert "+Offre Starter : 29 €/mois" in diff_content

def test_save_snapshot_multiple_urls_no_collision(tmp_path: Path):
    url_pricing = "https://competitor.example/pricing"
    url_changelog = "https://competitor.example/changelog"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    save_snapshot_and_diff(url_pricing, "Contenu Tarifs", out_dir=tmp_path)
    save_snapshot_and_diff(url_changelog, "Contenu Changelog", out_dir=tmp_path)

    pricing_file = tmp_path / "competitor.example" / "pricing" / f"{today}.txt"
    changelog_file = tmp_path / "competitor.example" / "changelog" / f"{today}.txt"

    assert pricing_file.exists()
    assert changelog_file.exists()
    assert pricing_file.read_text(encoding="utf-8") == "Contenu Tarifs"
    assert changelog_file.read_text(encoding="utf-8") == "Contenu Changelog"
