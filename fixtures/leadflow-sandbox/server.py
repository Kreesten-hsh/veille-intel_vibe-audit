#!/usr/bin/env python3
"""Serveur Mock Léger pour la Sandbox LeadFlow (Vibe-Audit Demo).

Utilise exclusivement la bibliothèque standard Python (zéro dépendance externe).
Reproduit fidèlement le comportement vulnérable documenté dans les rapports :
- Endpoint REST Supabase : /rest/v1/orders (RLS absent, Content-Range: 0-1/142)
- Absence des en-têtes CSP et X-Frame-Options
- En-tête CORS permissif : Access-Control-Allow-Origin: *
- Endpoint Stripe Webhook : /api/webhooks/stripe (non signé)
"""

import http.server
import json
import sys
from urllib.parse import parse_qs, urlparse

MOCK_ORDERS = [
    {"id": "ord_812", "customer_email": "m.***@gmail.com", "amount": 4900},
    {"id": "ord_813", "customer_email": "agence.***@pro.fr", "amount": 12900},
]
TOTAL_ORDERS_COUNT = 142


class LeadFlowSandboxHandler(http.server.BaseHTTPRequestHandler):
    """Gestionnaire HTTP reproduisant les comportements et failles de LeadFlow."""

    def log_message(self, format, *args):
        # Silence logs during automated tests unless verbose
        if "-v" in sys.argv:
            super().log_message(format, *args)

    def _set_vulnerable_headers(self, status=200, content_type="application/json"):
        """Émet les en-têtes HTTP de la sandbox (comportement par défaut vulnérable)."""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        # FAILLE SEC-03 : CORS permissif
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "apikey, Authorization, Content-Type")
        # NOTE : Absence volontaire de Content-Security-Policy et X-Frame-Options (SEC-03)

    def do_OPTIONS(self):
        """Réponse preflight CORS permissive."""
        self._set_vulnerable_headers(204)
        self.end_headers()

    def do_GET(self):
        """Simule les endpoints GET de l'application."""
        parsed = urlparse(self.path)

        if parsed.path == "/rest/v1/orders":
            # FAILLE SEC-01 : Fuite de données Supabase car RLS non activé sur orders
            self._set_vulnerable_headers(200, "application/json")
            # En-tête de pagination Supabase certifiant 142 commandes accessibles
            self.send_header("Content-Range", f"0-1/{TOTAL_ORDERS_COUNT}")
            self.end_headers()

            payload = json.dumps(MOCK_ORDERS, indent=2)
            self.wfile.write(payload.encode("utf-8"))
            return

        if parsed.path in ("/", "/index.html"):
            self._set_vulnerable_headers(200, "text/html; charset=utf-8")
            self.end_headers()
            html = """<!DOCTYPE html>
<html>
<head><title>LeadFlow Demo Sandbox</title></head>
<body>
  <h1>LeadFlow Dashboard (Demo Target)</h1>
  <p>Environnement de test contrôlé pour vérification Vibe-Audit.</p>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
            return

        self._set_vulnerable_headers(404, "application/json")
        self.end_headers()
        self.wfile.write(b'{"error": "Not Found"}')

    def do_POST(self):
        """Simule les endpoints POST, notamment le webhook Stripe."""
        parsed = urlparse(self.path)

        if parsed.path == "/api/webhooks/stripe":
            # FAILLE SEC-04 : Accepte le webhook Stripe sans vérification de signature
            content_length = int(self.headers.get("Content-Length", 0))
            body_raw = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"

            try:
                data = json.loads(body_raw)
            except json.JSONDecodeError:
                data = {}

            # Aucune vérification de l'en-tête stripe-signature
            self._set_vulnerable_headers(200, "application/json")
            self.end_headers()
            response = {"received": True, "vulnerability": "unsigned_webhook_accepted", "data": data}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        self._set_vulnerable_headers(404, "application/json")
        self.end_headers()
        self.wfile.write(b'{"error": "Not Found"}')


def run_server(port=8765):
    """Démarre le serveur local de simulation."""
    server_address = ("127.0.0.1", port)
    httpd = http.server.HTTPServer(server_address, LeadFlowSandboxHandler)
    print(f"[LeadFlow Sandbox] Serveur actif sur http://127.0.0.1:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[LeadFlow Sandbox] Arrêt du serveur.")
        httpd.server_close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    run_server(port)
