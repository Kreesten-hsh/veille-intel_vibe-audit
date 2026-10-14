"""Tests de validation de la cible de test LeadFlow Sandbox (fixtures/leadflow-sandbox).

Vérifie que la sandbox reproduit fidèlement et de manière contrôlée les 4 failles documentées :
1. SEC-01 : Schéma SQL avec RLS manquant sur la table orders
2. SEC-02 : Clé d'API Resend de production exposée dans le bundle client
3. SEC-03 : En-têtes HTTP de sécurité manquants (CSP, X-Frame-Options) et CORS permissif
4. SEC-04 : Webhook Stripe non signé
5. Simulation réseau : L'endpoint /rest/v1/orders renvoie exactement Content-Range: 0-1/142
"""

import http.client
import http.server
import json
import threading
from pathlib import Path
import pytest

import importlib.util

SANDBOX_DIR = Path("fixtures/leadflow-sandbox")
server_path = (SANDBOX_DIR / "server.py").resolve()
spec = importlib.util.spec_from_file_location("leadflow_server", server_path)
leadflow_server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(leadflow_server)
LeadFlowSandboxHandler = leadflow_server.LeadFlowSandboxHandler



def test_sandbox_files_exist():
    """Vérifie que tous les artefacts de la sandbox sont en place."""
    assert (SANDBOX_DIR / "README.md").exists()
    assert (SANDBOX_DIR / "supabase/schema.sql").exists()
    assert (SANDBOX_DIR / "src/config.ts").exists()
    assert (SANDBOX_DIR / "src/lib/resend.ts").exists()
    assert (SANDBOX_DIR / "api/stripe-webhook.js").exists()
    assert (SANDBOX_DIR / "server.py").exists()


def test_sec01_supabase_rls_flaw():
    """Vérifie que la table orders n'a pas de RLS activé dans le schéma SQL."""
    schema = (SANDBOX_DIR / "supabase/schema.sql").read_text(encoding="utf-8")
    assert "CREATE TABLE IF NOT EXISTS orders" in schema
    # Vérifie que users a bien le RLS (contrôle positif) mais orders ne l'a pas (faille)
    assert "ALTER TABLE users ENABLE ROW LEVEL SECURITY;" in schema
    assert "ALTER TABLE orders ENABLE ROW LEVEL SECURITY;" not in schema


def test_sec02_resend_key_exposure():
    """Vérifie l'exposition de la clé privée Resend dans les fichiers front-end."""
    config = (SANDBOX_DIR / "src/config.ts").read_text(encoding="utf-8")
    assert "re_live_" in config
    assert "RESEND_API_KEY" in config

    resend_lib = (SANDBOX_DIR / "src/lib/resend.ts").read_text(encoding="utf-8")
    assert "api.resend.com" in resend_lib
    assert "CONFIG.RESEND_API_KEY" in resend_lib


def test_sec04_stripe_webhook_unsigned():
    """Vérifie que le webhook Stripe ne vérifie pas la signature cryptographique."""
    webhook_code = (SANDBOX_DIR / "api/stripe-webhook.js").read_text(encoding="utf-8")
    assert "constructEvent" not in webhook_code
    assert "stripe-signature" not in webhook_code


@pytest.fixture(scope="module")
def running_sandbox_server():
    """Démarre le serveur mock sur un port éphémère (0) pendant la session de test."""
    server = http.server.HTTPServer(("127.0.0.1", 0), LeadFlowSandboxHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"127.0.0.1:{port}"
    server.shutdown()
    server.server_close()


def test_sec01_and_sec03_server_http_behavior(running_sandbox_server):
    """Vérifie le comportement HTTP réel du serveur mock : Content-Range et headers de sécurité."""
    host, port = running_sandbox_server.split(":")
    conn = http.client.HTTPConnection(host, int(port))

    # Test GET /rest/v1/orders
    conn.request("GET", "/rest/v1/orders?select=id,customer_email,amount&limit=2")
    res = conn.getresponse()
    body = res.read().decode("utf-8")

    assert res.status == 200
    headers = dict(res.getheaders())

    # SEC-01 : Preuve de pagination avec 142 commandes
    assert headers.get("Content-Range") == "0-1/142"

    # SEC-03 : Headers manquants et CORS permissif
    assert headers.get("Access-Control-Allow-Origin") == "*"
    assert "Content-Security-Policy" not in headers
    assert "X-Frame-Options" not in headers

    # Vérification du corps de réponse (données de test)
    data = json.loads(body)
    assert len(data) == 2
    assert data[0]["id"] == "ord_812"
    assert data[0]["amount"] == 4900
    assert data[1]["id"] == "ord_813"


def test_sec04_server_stripe_webhook_accepts_unsigned(running_sandbox_server):
    """Vérifie que le serveur mock accepte les requêtes de webhook sans signature."""
    host, port = running_sandbox_server.split(":")
    conn = http.client.HTTPConnection(host, int(port))

    fake_payload = json.dumps({
        "type": "checkout.session.completed",
        "data": {"object": {"customer_email": "test@pro.fr"}},
    })
    conn.request(
        "POST",
        "/api/webhooks/stripe",
        body=fake_payload,
        headers={"Content-Type": "application/json"},
    )
    res = conn.getresponse()
    body = res.read().decode("utf-8")

    assert res.status == 200
    data = json.loads(body)
    assert data.get("received") is True
    assert data.get("vulnerability") == "unsigned_webhook_accepted"


def test_scan_vibe_detects_all_sandbox_flaws():
    """Vérifie que scan_vibe détecte automatiquement les failles de la sandbox."""
    from scripts.scan_vibe import scan_directory

    findings = scan_directory(SANDBOX_DIR)
    refs = {f["ref"] for f in findings}
    locations = [f["location"] for f in findings]

    assert "SEC-01" in refs
    assert "SEC-02" in refs
    assert "SEC-04" in refs

    assert any("supabase/schema.sql" in loc for loc in locations)
    assert any("src/config.ts" in loc for loc in locations)
    assert any("api/stripe-webhook.js" in loc for loc in locations)
