# Tâches d'Implémentation : Moteur de Veille Concurrentielle Passive (veille-intel)

**Spécification** : [spec.md](spec.md) | **Plan** : [plan.md](plan.md)  
**Règle d'exécution** : Un seul lot à la fois avec ses tests. Arrêt obligatoire pour validation humaine après chaque lot.

---

## Lot A (Maintenant) : Script Unique de Capture & Test

**Objectif** : Un script unique `scripts/capture.py` (respect robots.txt, délai 5 s, User-Agent transparent, extraction du texte, SHA-256, date), plus un test. Rien d'autre.

- [ ] T001 [Test] Écrire le test unitaire pour `scripts/capture.py` dans `tests/test_capture.py` (validation du respect de robots.txt, temporisation de 5 s mockée, User-Agent transparent, extraction du texte épuré et empreinte SHA-256 avec date).
- [ ] T002 [Impl] Implémenter le script unique autonome `scripts/capture.py` effectuant la capture passive respectueuse, le calcul de hash SHA-256 et l'horodatage.

---

## Lot B (Différé jusqu'au premier virement reçu) : Diff, Rapport HTML, CLI

**Objectif** : Finalisation du moteur complet après confirmation du premier encaissement réel par virement bancaire.

- [ ] T003 Moteur différentiel N vs N-1 (calcul de delta textuel et catégorisation des signaux).
- [ ] T004 Générateur de livrable en marque blanche (gabarit Jinja2, rendu HTML autonome et export PDF).
- [ ] T005 Interface en ligne de commande unifiée (CLI pour orchestrer l'ensemble des étapes).

---

## Archivé : remplacé, trop lourd avant la première vente

### [ARCHIVÉ] Lot 1 : Fondations & Persistance Locale (Setup & Foundational)
- [ ] T001 [P] Créer `pyproject.toml` avec les dépendances déclarées (`httpx`, `beautifulsoup4`, `jinja2`, `pyyaml`, `pytest`).
- [ ] T002 [P] Initialiser l'arborescence du projet (`src/veille/`, `templates/veille/`, `tests/fixtures/`, `data/`).
- [ ] T003 [US1] Écrire les tests unitaires pour la configuration des cibles dans `tests/test_config.py`.
- [ ] T004 [US1] Écrire les tests unitaires pour la persistance SQLite dans `tests/test_storage.py`.
- [ ] T005 [US1] Implémenter le validateur de configuration dans `src/veille/config.py`.
- [ ] T006 [US1] Implémenter le gestionnaire SQLite (tables `targets`, `snapshots`, `diff_events`) dans `src/veille/storage.py`.

### [ARCHIVÉ] Lot 2 : Collecte Passive & Respect Éthique (User Story 1 - P1 MVP)
- [ ] T007 [P] [US1] Créer les fixtures `tests/fixtures/robots_allow.txt`, `tests/fixtures/robots_disallow.txt` et `tests/fixtures/page_v1.html`.
- [ ] T008 [US1] Écrire les tests unitaires du collecteur passif dans `tests/test_fetcher.py` (vérification robots.txt, gestion des erreurs HTTP, calcul du hash).
- [ ] T009 [US1] Implémenter le fetcher passif et poli dans `src/veille/fetcher.py`.
- [ ] T010 [US1] Intégrer l'ingestion avec `storage.py` pour enregistrer les instantanés horodatés.

### [ARCHIVÉ] Lot 3 : Moteur de Diff & Classification Déterministe (User Story 2 - P2)
- [ ] T011 [P] [US2] Créer les fixtures `tests/fixtures/page_v2_price_change.html` et `tests/fixtures/page_v2_redesign.html`.
- [ ] T012 [US2] Écrire les tests unitaires d'épuration HTML, de diff et de classification dans `tests/test_diff_engine.py`.
- [ ] T013 [US2] Implémenter le nettoyage du DOM et l'extraction de texte dans `src/veille/diff_engine.py`.
- [ ] T014 [US2] Implémenter le calcul de delta structuré et les heuristiques de classification par mots-clés dans `src/veille/diff_engine.py`.

### [ARCHIVÉ] Lot 4 : Livrable Marque Blanche & Interface CLI (User Story 3 - P3)
- [ ] T015 [P] [US3] Écrire les tests unitaires du générateur de rapport dans `tests/test_reporter.py`.
- [ ] T016 [US3] Écrire le test d'intégration de bout en bout (CLI complète offline) dans `tests/test_e2e_pipeline.py`.
- [ ] T017 [US3] Concevoir le gabarit Jinja2 autonome responsive dans `templates/veille/report_template.html`.
- [ ] T018 [US3] Implémenter le compilateur de rapport dans `src/veille/reporter.py`.
- [ ] T019 Implémenter la CLI complète (`fetch`, `diff`, `report`, `run-weekly`) dans `src/veille/cli.py`.
