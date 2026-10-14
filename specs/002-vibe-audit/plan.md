# Plan d'Implémentation : Vibe-Audit

## 1. Architecture des Composants

```
templates/
└── vibe-audit/
    ├── template-rapport.html      # Gabarit HTML/CSS exécutif pour génération PDF
    ├── formulaire-consentement.md  # Modèle d'accord bilatéral NDA & autorisation
    └── prompts-bibliotheque.json  # Bibliothèque des prompts types de remédiation
scripts/
└── vibe-audit/
    ├── check_headers.py           # Analyseur passif des headers HTTP & CORS
    ├── check_exposed_keys.py      # Scanner passif d'empreintes de clés secrètes dans bundles JS
    └── generate_report.py         # Compilateur HTML ➔ PDF du rapport exécutif
fixtures/
└── realistic-vulnerable-app/     # Application réaliste simulant une app Lovable/Bolt
    ├── frontend/                  # App React/Vite avec fausses clés et appels Supabase
    └── backend/                   # Edge function avec webhook Stripe vulnérable
```

## 2. Décisions d'Architecture
- **Génération PDF** : Utilisation d'un template HTML/CSS imprimable moderne converti via Headless Chrome ou WeasyPrint pour un rendu typographique parfait sans bibliothèque lourde payante.
- **Application de Test Réaliste** : Remplacer l'ancienne app par une application simulant exactement un Micro-SaaS d'IA moderne (ex: un outil de transcription ou d'audit de CV utilisant Supabase + Stripe).
- **Processus de Vente 100% Asynchrone** : Zéro appel téléphonique ou vidéo. Toute la vente et le support passent par message écrit (Email & LinkedIn direct), réduisant la friction et augmentant le débit opérationnel.
