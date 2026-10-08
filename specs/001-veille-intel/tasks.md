# Tâches d'Implémentation : Moteur de Veille Concurrentielle Passive (veille-intel)

**Spécification** : [spec.md](file:///home/hasashi/Bureau/veille-intel_vibe-audit/specs/001-veille-intel/spec.md) | **Plan** : [plan.md](file:///home/hasashi/Bureau/veille-intel_vibe-audit/specs/001-veille-intel/plan.md)  
**Règle d'exécution** : Un seul lot à la fois avec ses tests. Arrêt obligatoire pour validation humaine après chaque lot.

---

## Lot 1 : Fondations & Persistance Locale (Setup & Foundational)

**Objectif** : Mettre en place l'environnement, le schéma de configuration et la persistance SQLite locale nécessaire à tous les modules.  
**Indépendant & Testable** : Testable à 100 % hors-ligne avec base SQLite en mémoire et fichiers YAML/JSON synthétiques.

### Tests pour le Lot 1 (Test-First)
- [ ] T001 [P] Créer `pyproject.toml` avec les dépendances déclarées (`httpx`, `beautifulsoup4`, `jinja2`, `pyyaml`, `pytest`).
- [ ] T002 [P] Initialiser l'arborescence du projet (`src/veille/`, `templates/veille/`, `tests/fixtures/`, `data/`).
- [ ] T003 [US1] Écrire les tests unitaires pour la configuration des cibles dans `tests/test_config.py`.
- [ ] T004 [US1] Écrire les tests unitaires pour la persistance SQLite dans `tests/test_storage.py`.

### Implémentation pour le Lot 1
- [ ] T005 [US1] Implémenter le validateur de configuration dans `src/veille/config.py`.
- [ ] T006 [US1] Implémenter le gestionnaire SQLite (tables `targets`, `snapshots`, `diff_events`) dans `src/veille/storage.py`.

**Point d'Arrêt Lot 1** : Exécution de `pytest tests/test_config.py tests/test_storage.py`. Présentation des résultats à l'opérateur avant de continuer.

---

## Lot 2 : Collecte Passive & Respect Éthique (User Story 1 - P1 MVP)

**Objectif** : Implémenter l'ingestion passive respectueuse (robots.txt, espacement 5s, User-Agent honnête, hash SHA-256).  
**Indépendant & Testable** : Testable hors-ligne via des mocks HTTP et des fixtures de `robots.txt`.

### Tests pour le Lot 2 (Test-First)
- [ ] T007 [P] [US1] Créer les fixtures `tests/fixtures/robots_allow.txt`, `tests/fixtures/robots_disallow.txt` et `tests/fixtures/page_v1.html`.
- [ ] T008 [US1] Écrire les tests unitaires du collecteur passif dans `tests/test_fetcher.py` (vérification robots.txt, gestion des erreurs HTTP, calcul du hash).

### Implémentation pour le Lot 2
- [ ] T009 [US1] Implémenter le fetcher passif et poli dans `src/veille/fetcher.py`.
- [ ] T010 [US1] Intégrer l'ingestion avec `storage.py` pour enregistrer les instantanés horodatés.

**Point d'Arrêt Lot 2** : Exécution de `pytest tests/test_fetcher.py`. Validation opérateur.

---

## Lot 3 : Moteur de Diff & Classification Déterministe (User Story 2 - P2)

**Objectif** : Nettoyer le contenu HTML (suppression du bruit), calculer les deltas entre instantanés et classifier les signaux d'affaires sans aucun LLM externe.  
**Indépendant & Testable** : Testable avec des paires de pages HTML représentatives (variations de prix, ajouts de services).

### Tests pour le Lot 3 (Test-First)
- [ ] T011 [P] [US2] Créer les fixtures `tests/fixtures/page_v2_price_change.html` et `tests/fixtures/page_v2_redesign.html`.
- [ ] T012 [US2] Écrire les tests unitaires d'épuration HTML, de diff et de classification dans `tests/test_diff_engine.py`.

### Implémentation pour le Lot 3
- [ ] T013 [US2] Implémenter le nettoyage du DOM et l'extraction de texte dans `src/veille/diff_engine.py`.
- [ ] T014 [US2] Implémenter le calcul de delta structuré et les heuristiques de classification par mots-clés dans `src/veille/diff_engine.py`.

**Point d'Arrêt Lot 3** : Exécution de `pytest tests/test_diff_engine.py`. Validation opérateur.

---

## Lot 4 : Livrable Marque Blanche & Interface CLI (User Story 3 - P3)

**Objectif** : Produire un rapport HTML autonome et esthétique aux couleurs de l'agence cliente et fournir la CLI unifiée.  
**Indépendant & Testable** : Testable en vérifiant la validité du HTML produit et l'exécution de bout en bout de la CLI.

### Tests pour le Lot 4 (Test-First)
- [ ] T015 [P] [US3] Écrire les tests unitaires du générateur de rapport dans `tests/test_reporter.py`.
- [ ] T016 [US3] Écrire le test d'intégration de bout en bout (CLI complète offline) dans `tests/test_e2e_pipeline.py`.

### Implémentation pour le Lot 4
- [ ] T017 [US3] Concevoir le gabarit Jinja2 autonome responsive dans `templates/veille/report_template.html`.
- [ ] T018 [US3] Implémenter le compilateur de rapport dans `src/veille/reporter.py`.
- [ ] T019 Implémenter la CLI complète (`fetch`, `diff`, `report`, `run-weekly`) dans `src/veille/cli.py`.

**Point d'Arrêt Final** : Suite complète `pytest` au vert. Démonstration de la production d'un rapport de démonstration.
