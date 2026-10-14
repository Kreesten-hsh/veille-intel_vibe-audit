#!/usr/bin/env python3
"""Scanner statique local pour Vibe-Audit.

Détecte les vulnérabilités courantes dans les dépôts d'applications créées avec
Lovable, Bolt, Cursor ou des outils no-code/IA :
1. Clés privées et secrets exposés (Resend, Stripe, Supabase service_role, tokens)
2. Tables SQL sans Row Level Security (RLS) ou avec des règles permissives
3. Webhooks Stripe traitant des paiements sans vérification cryptographique (constructEvent)

Bibliothèque standard Python exclusivement (zéro dépendance externe).
"""

import json
import re
import sys
from pathlib import Path

IGNORED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
    "venv",
    ".venv",
    ".pytest_cache",
}

VALID_EXTENSIONS = {".js", ".ts", ".tsx", ".py", ".sql", ".env"}


def is_scannable(p: Path) -> bool:
    """Vérifie si le fichier fait partie du périmètre de scan."""
    if any(part in IGNORED_DIRS for part in p.parts):
        return False
    if p.name.startswith(".env"):
        return True
    return p.suffix.lower() in VALID_EXTENSIONS


def scan_secrets(file_path: Path, rel_path: str, lines: list[str]) -> list[dict]:
    """Détecte les clés secrètes et tokens privés dans le fichier."""
    findings = []
    # Patterns de détection de secrets
    secret_patterns = [
        (
            re.compile(r"""(?:["']|\b)(re_live_[a-zA-Z0-9_\-]{16,})"""),
            "high",
            "SEC-02",
            "Clé secrète Resend de production exposée dans le code source",
        ),
        (
            re.compile(r"""(?:["']|\b)(sk_live_[a-zA-Z0-9_\-]{16,})"""),
            "critical",
            "SEC-02",
            "Clé secrète Stripe de production (sk_live_) exposée en clair",
        ),
        (
            re.compile(r"""(?:SUPABASE_SERVICE_ROLE_KEY|SERVICE_ROLE_KEY)\s*[:=]\s*["']?([A-Za-z0-9_\-\.]{20,})"""),
            "critical",
            "SEC-02",
            "Clé d'administration Supabase (service_role) exposée",
        ),
        (
            re.compile(r"""(?:RESEND_API_KEY|RESEND_KEY)\s*[:=]\s*["'](re_[a-zA-Z0-9_\-]+)["']"""),
            "high",
            "SEC-02",
            "Clé d'API Resend exposée dans la configuration",
        ),
    ]

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Éviter les lignes de commentaires documentaires purs
        if stripped.startswith("//") and not any(kw in stripped for kw in ("=", ":")):
            continue
        if stripped.startswith("#") and not any(kw in stripped for kw in ("=", ":")):
            continue

        for pattern, severity, ref, title in secret_patterns:
            if pattern.search(stripped):
                findings.append({
                    "ref": ref,
                    "severity": severity,
                    "title": title,
                    "location": f"{rel_path}:{idx}",
                    "evidence": stripped,
                })
                break
    return findings


def scan_sql_rls(file_path: Path, rel_path: str, content: str, lines: list[str]) -> list[dict]:
    """Détecte les tables créées sans RLS ou avec des politiques permissives."""
    findings = []

    # 1. Recherche des tables créées
    created_tables: list[tuple[str, int, str]] = []
    for idx, line in enumerate(lines, start=1):
        m = re.search(r"""CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_"]+)""", line, re.IGNORECASE)
        if m:
            tbl = m.group(1).strip('"').lower()
            created_tables.append((tbl, idx, line.strip()))

    # 2. Recherche des tables protégées par RLS
    enabled_tables: set[str] = set()
    for m in re.finditer(r"""ALTER\s+TABLE\s+(?:ONLY\s+)?(?:IF\s+EXISTS\s+)?([a-zA-Z0-9_"]+)\s+ENABLE\s+ROW\s+LEVEL\s+SECURITY""", content, re.IGNORECASE):
        enabled_tables.add(m.group(1).strip('"').lower())

    # Signalement des tables sans RLS
    for tbl, line_idx, raw_line in created_tables:
        if tbl not in enabled_tables:
            findings.append({
                "ref": "SEC-01",
                "severity": "high",
                "title": f"Absence de Row Level Security (RLS) sur la table '{tbl}'",
                "location": f"{rel_path}:{line_idx}",
                "evidence": raw_line,
            })

    # 3. Détection des politiques permissives USING (true)
    for idx, line in enumerate(lines, start=1):
        if re.search(r"""USING\s*\(\s*true\s*\)""", line, re.IGNORECASE):
            findings.append({
                "ref": "SEC-01",
                "severity": "high",
                "title": f"Politique RLS permissive USING (true) accordant un accès universel",
                "location": f"{rel_path}:{idx}",
                "evidence": line.strip(),
            })

    return findings


def scan_stripe_webhooks(file_path: Path, rel_path: str, content: str, lines: list[str]) -> list[dict]:
    """Détecte les webhooks Stripe sans vérification de signature constructEvent."""
    findings = []
    lower_path = rel_path.lower()
    is_webhook_file = "webhook" in lower_path or "stripe" in lower_path

    # Détecte la présence de traitement d'événements Stripe
    handles_stripe = (
        "checkout.session" in content
        or "handleStripeWebhook" in content
        or "stripe.webhooks" in content
        or "customer.subscription" in content
        or (is_webhook_file and "stripe" in content.lower())
    )

    if handles_stripe and "constructEvent" not in content:
        # Trouver la ligne la plus représentative de l'entrée du webhook
        handler_line = 1
        handler_evidence = lines[0].strip() if lines else ""
        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()
            if any(term in stripped for term in ("handleStripeWebhook", "function", "def ", "router.post", "app.post")):
                handler_line = idx
                handler_evidence = stripped
                break
            elif "checkout.session" in stripped:
                handler_line = idx
                handler_evidence = stripped
                break

        findings.append({
            "ref": "SEC-04",
            "severity": "high",
            "title": "Webhook Stripe sans vérification de signature cryptographique (constructEvent manquant)",
            "location": f"{rel_path}:{handler_line}",
            "evidence": handler_evidence,
        })

    return findings


def scan_directory(target_dir: Path) -> list[dict]:
    """Scanne récursivement le dossier cible pour toutes les failles répertoriées."""
    findings = []
    target_dir = target_dir.resolve()

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"[ERREUR] Le dossier spécifié n'existe pas : {target_dir}", file=sys.stderr)
        return []

    for file_path in sorted(target_dir.rglob("*")):
        if not file_path.is_file() or not is_scannable(file_path):
            continue

        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()
            rel_path = str(file_path.relative_to(target_dir))
        except Exception as e:
            print(f"[AVERTISSEMENT] Impossible de lire {file_path} : {e}", file=sys.stderr)
            continue

        # 1. Analyse des secrets
        findings.extend(scan_secrets(file_path, rel_path, lines))

        # 2. Analyse SQL RLS
        if file_path.suffix.lower() == ".sql":
            findings.extend(scan_sql_rls(file_path, rel_path, content, lines))

        # 3. Analyse des webhooks Stripe
        if file_path.suffix.lower() in (".js", ".ts", ".tsx", ".py"):
            findings.extend(scan_stripe_webhooks(file_path, rel_path, content, lines))

    return findings


def main():
    target_arg = sys.argv[1] if len(sys.argv) > 1 else "fixtures/leadflow-sandbox"
    target_dir = Path(target_arg)
    findings = scan_directory(target_dir)
    print(json.dumps(findings, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
