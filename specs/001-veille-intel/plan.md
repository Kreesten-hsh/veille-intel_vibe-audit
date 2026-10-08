# Plan d'Implémentation : Moteur de Veille Concurrentielle Passive (veille-intel)

**Branche** : `001-veille-intel` | **Date** : 2026-10-08 | **Spécification** : [spec.md](spec.md)

---

## Résumé Technique

Implémentation d'un moteur de veille concurrentielle passif en Python 3.12 pur, opérant en 4 modules déterministes sans aucune API LLM externe :
1. `config` : Chargement et validation des cibles de surveillance (YAML / JSON).
2. `fetcher` : Client HTTP passif poli (`httpx`), validation stricte `robots.txt` (`urllib.robotparser`), temporisation de 5 secondes, hashing SHA-256 et persistance SQLite (`data/veille.db`).
3. `diff_engine` : Extraction du texte épuré (BeautifulSoup), calcul de deltas textuels/structurels (`difflib` standard), classification heuristique déterministe en 4 catégories d'affaires.
4. `reporter` : Injection des signaux dans un gabarit HTML autonome Jinja2 personnalisable en marque blanche (logo, palette, mentions).

---

## Contexte Technique

- **Langage / Version** : Python 3.12 (environnement géré par `uv`).
- **Dépendances Principales** :
  - `httpx` : Client HTTP synchrone robuste avec gestion des timeouts.
  - `beautifulsoup4` : Épuration du DOM, élimination des bruits scripts/styles/nonces.
  - `jinja2` : Moteur de templating pour le livrable HTML marque blanche.
  - `pyyaml` : Parsing des fichiers de configuration clients.
  - `pytest` : Suite de tests automatisés.
- **Stockage** : SQLite 3 (`data/veille.db`), tables : `targets`, `snapshots`, `diff_events`, `reports`.
- **Plateforme Cible** : Linux (Ubuntu/Debian) - exécution locale en ligne de commande.
- **Contraintes** :
  - Zéro appel réseau payant, zéro dépendance cloud.
  - 100 % des tests exécutables hors-ligne sans connexion internet.
  - Production d'un livrable complet en moins de 45 minutes opérateur par client.

---

## Contrôle de Conformité Constitutionnelle (Constitution Check)

| Règle Constitutionnelle | Statut | Justification |
| :--- | :---: | :--- |
| **I. Zéro Dépense & Zéro Dette** | **CONFORME** | Dépendances 100% open source libres (MIT/BSD/Apache), aucun modèle LLM payant, zéro carte bancaire. |
| **II. Éthique Passive & Robots.txt** | **CONFORME** | Vérification systématique de `robots.txt`, délai de 5s entre requêtes, User-Agent transparent, aucun contournement. |
| **III. Local-First & Confidentialité** | **CONFORME** | Toutes les données restent dans `data/veille.db` local, `.gitignore` protège secrets et données. |
| **IV. Déterminisme & Zéro Hallucination** | **CONFORME** | Pas de génération aléatoire : faits bruts observables, diffs exacts, classification par mots-clés pondérés. |
| **V. Test-First & Découpage en Lots** | **CONFORME** | Suite de tests par lot avec fixtures HTML locales, approbation opérateur obligatoire avant chaque lot. |

---

## Structure du Code

```text
src/
└── veille/
    ├── __init__.py
    ├── cli.py             # Point d'entrée CLI (fetch, diff, report, run-weekly)
    ├── config.py          # Validation des fichiers de configuration cibles
    ├── storage.py         # Gestionnaire SQLite (schema, transactions, snapshots)
    ├── fetcher.py         # Ingestion passive, robots.txt, temporisation 5s
    ├── diff_engine.py     # Nettoyage HTML, calcul de delta, classification
    └── reporter.py        # Rendu Jinja2 en marque blanche

templates/
└── veille/
    └── report_template.html  # Gabarit HTML moderne responsive, prêt pour impression PDF

tests/
├── conftest.py            # Fixtures de test réutilisables (DB en mémoire, mocks HTML)
├── fixtures/
│   ├── robots_allow.txt
│   ├── robots_disallow.txt
│   ├── page_v1.html
│   └── page_v2_price_change.html
├── test_config.py
├── test_fetcher.py
├── test_storage.py
├── test_diff_engine.py
└── test_reporter.py
```

---

## Découpage de l'Implémentation en Lots (Phases)

- **Lot 1 : Fondations & Persistance** (`config.py`, `storage.py`, schéma SQLite, tests unitaires).
- **Lot 2 : Collecte Passive & Éthique** (`fetcher.py`, vérification robots.txt, pacing 5s, tests avec mocks).
- **Lot 3 : Moteur de Diff & Classification** (`diff_engine.py`, épuration HTML, deltas structurés, tests de précision).
- **Lot 4 : Génération de Rapport Marque Blanche & CLI** (`reporter.py`, `templates/`, `cli.py`, tests de rendu E2E).
