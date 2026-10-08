# Graph Report - veille-intel_vibe-audit  (2026-10-08)

## Corpus Check
- 55 files · ~55,903 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 1, .csv 1)

## Summary
- 567 nodes · 726 edges · 40 communities (37 shown, 3 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Jalons et Points d'Arrêt Décisionnels (Gates)
- Déroulement Pas à Pas
- 1. Veille-Intel (Agences Marketing)
- Cadre Légal, Réglementaire et Conformité RGPD
- 1. Offre : Veille-Intel (Veille Concurrentielle Marque Blanche)
- PRD Unifié : Veille-Intel & Vibe-Audit
- Projet vibe-audit
- Project Profile: veille-intel_vibe-audit
- Projet Unifié : Veille-Intel & Vibe-Audit
- Grille Tarifaire et Conditions Commerciales
- SKILLS_INDEX.md
- FACTURE-TEMPLATE.md
- common.py
- Boîte à Outils Autorisée et Liste Fermée (Outils Retenus & Écartés)
- 1.2 Déroulement Étape par Étape
- 3. Décisions d'Architecture (Architecture Decision Records - ADR)
- Stratégie de Test & Assurance Qualité
- common.sh
- Stratégie Go-to-Marché & Prospection Manuelle B2B
- Modélisation Financière, Calendrier d'Encaissement & Scénarios
- Cadre Juridique, Confidentialité des Données & Conformité Réglementaire
- Protocole de Consentement et d'Autorisation d'Audit Technique
- Tasks: [FEATURE NAME]
- speckit-analyze/SKILL.md
- create_new_feature.py
- Execution Steps
- Feature Specification: [FEATURE NAME]
- speckit-plan/SKILL.md
- speckit-specify/SKILL.md
- speckit-tasks/SKILL.md
- Core Principles
- Core Principles
- Implementation Plan: [FEATURE]
- speckit-checklist/SKILL.md
- speckit-clarify/SKILL.md
- speckit-implement/SKILL.md
- speckit-constitution/SKILL.md
- speckit-taskstoissues/SKILL.md
- [CHECKLIST TYPE] Checklist: [FEATURE NAME]

## God Nodes (most connected - your core abstractions)
1. `resolve_template_content()` - 20 edges
2. `TemplateResolutionError` - 17 edges
3. `main()` - 15 edges
4. `PRD Unifié : Veille-Intel & Vibe-Audit` - 15 edges
5. `get_feature_paths()` - 14 edges
6. `Tasks: [FEATURE NAME]` - 13 edges
7. `main()` - 11 edges
8. `create-new-feature.sh script` - 10 edges
9. `main()` - 10 edges
10. `get_repo_root()` - 9 edges

## Surprising Connections (you probably didn't know these)
- `main()` --uses--> `TemplateResolutionError`  [INFERRED]
  .specify/scripts/python/create_new_feature.py → .specify/scripts/python/common.py
- `_available_docs()` --uses--> `FeaturePaths`  [INFERRED]
  .specify/scripts/python/check_prerequisites.py → .specify/scripts/python/common.py
- `_print_paths_only()` --uses--> `FeaturePaths`  [INFERRED]
  .specify/scripts/python/check_prerequisites.py → .specify/scripts/python/common.py
- `_print_text_results()` --uses--> `FeaturePaths`  [INFERRED]
  .specify/scripts/python/check_prerequisites.py → .specify/scripts/python/common.py
- `main()` --uses--> `TemplateResolutionError`  [INFERRED]
  .specify/scripts/python/check_prerequisites.py → .specify/scripts/python/common.py

## Import Cycles
- None detected.

## Communities (40 total, 3 thin omitted)

### Community 1 - "Jalons et Points d'Arrêt Décisionnels (Gates)"
Cohesion: 0.17
Nodes (11): 1. Principes d'Arrêt et Garde-fous Économiques, 2. Jalon 1 : Validation de l'Intérêt Marché (Date cible : ~24 octobre 2026), 3. Jalon 2 : Validation de la Monétisation (Date cible : ~10 novembre 2026), 4. Tableau de Synthèse des Jalons, Critères de Succès Minima (Go / No-Go), Critères de Succès Minima (Go / No-Go), Décisions à Prendre au Jalon 1, Décisions à Prendre au Jalon 2 (+3 more)

### Community 2 - "Déroulement Pas à Pas"
Cohesion: 0.11
Nodes (17): 1. Cycle Opérationnel : Veille-Intel (Hebdomadaire), 2. Cycle Opérationnel : Vibe-Audit (Mission 48h), 3. Gestion des Incidents & Cas Dégradés, Déroulement Pas à Pas, Déroulement Pas à Pas, Guide Opérationnel de l'Opérateur (Runbook), Objectif de Temps, Étape 1 : Initialisation & Configuration (Lundi 08h00) (+9 more)

### Community 3 - "1. Veille-Intel (Agences Marketing)"
Cohesion: 0.20
Nodes (9): 1. Veille-Intel (Agences Marketing), 2. Vibe-Audit (Fondateurs d'Apps Lovable / Bolt / Cursor), Message Initial (Fondateur), Message Initial (Prise de contact directe), Relance Unique (J+4 ou J+5 ouvrés), Relance Unique (J+4 ou J+5 ouvrés), Réponse à l'objection : « Pourquoi payer alors qu'on peut demander à l'IA (ou au chatbot) d'auditer le code gratuitement ? », Réponse à l'objection : « Pourquoi payer alors qu'on peut utiliser une IA gratuite (ChatGPT, Perplexity) ? » (+1 more)

### Community 4 - "Cadre Légal, Réglementaire et Conformité RGPD"
Cohesion: 0.22
Nodes (8): 1. Protocole de Consentement Obligatoire (Vibe-Audit), 2. Scraping Éthique et Sources Publiques (Veille-Intel), 3. Prospection Commerciale B2B et RGPD, 4. Points de Vigilance à Vérifier auprès de la CNIL ou d'un Avocat, Base Légale : L'Intérêt Légitime, Cadre Légal, Réglementaire et Conformité RGPD, Droit d'Opposition et Transparence, Modalités

### Community 5 - "1. Offre : Veille-Intel (Veille Concurrentielle Marque Blanche)"
Cohesion: 0.14
Nodes (13): 1. Offre : Veille-Intel (Veille Concurrentielle Marque Blanche), 2. Offre : Vibe-Audit (Audit Express de Sécurité pour Apps IA), Cible, Cible, Contexte & Problème, Contexte & Problème, Engagements Opérationnels, Entrées Fournies par l'Agence (+5 more)

### Community 6 - "PRD Unifié : Veille-Intel & Vibe-Audit"
Cohesion: 0.06
Nodes (30): 10. Métriques de succès et points d'arrêt (Chiffrés et datés), 11. Registre d'hypothèses, 12. Risques et mitigations, 13. Hors périmètre, 14. Questions ouvertes, 1. Résumé exécutif, 2.1 Objectifs financiers et règle de calendrier, 2.2 Objectifs produit (+22 more)

### Community 7 - "Projet vibe-audit"
Cohesion: 0.08
Nodes (24): Acquisition, Acquisition, Arithmétique, Arithmétique, Contexte commun, Contraintes absolues, Le business, Le business (+16 more)

### Community 8 - "Project Profile: veille-intel_vibe-audit"
Cohesion: 0.40
Nodes (4): 1. Stack & Architecture, 2. Resource Affinity (Auto-Routed), 3. Local Constraints & Conventions, Project Profile: veille-intel_vibe-audit

### Community 9 - "Projet Unifié : Veille-Intel & Vibe-Audit"
Cohesion: 0.40
Nodes (4): Garde-fous et Principes Directeurs, Organisation de la Documentation (`docs/`), Projet Unifié : Veille-Intel & Vibe-Audit, Vue d'Ensemble des Deux Piliers

### Community 10 - "Grille Tarifaire et Conditions Commerciales"
Cohesion: 0.40
Nodes (4): 1. Tarifs : Veille-Intel, 2. Tarifs : Vibe-Audit, 3. Modalités de Facturation et Règlement, Grille Tarifaire et Conditions Commerciales

### Community 13 - "common.py"
Cohesion: 0.07
Nodes (68): argparse, dataclasses, json, os, pathlib, RuntimeError, Args, _available_docs() (+60 more)

### Community 14 - "Boîte à Outils Autorisée et Liste Fermée (Outils Retenus & Écartés)"
Cohesion: 0.40
Nodes (4): 1. Inventaire et Évaluation des Outils Candidats, 2. Skills à Invoquer par Tâche (8 Skills Actifs au Maximum), 3. Décisions Opérateur & Arbitrages Validés, Boîte à Outils Autorisée et Liste Fermée (Outils Retenus & Écartés)

### Community 15 - "1.2 Déroulement Étape par Étape"
Cohesion: 0.08
Nodes (25): 1.1 Objectifs de Temps, 1.2 Déroulement Étape par Étape, 1. Procédure Pas à Pas : Veille-Intel (Abonnement Hebdomadaire), 2.1 Objectifs de Temps, 2.2 Déroulement Étape par Étape, 2. Procédure Pas à Pas : Vibe-Audit (Mission Express 48 h), 3.1 Checklist Pré-Livraison : Veille-Intel, 3.2 Checklist Pré-Livraison : Vibe-Audit (+17 more)

### Community 16 - "3. Décisions d'Architecture (Architecture Decision Records - ADR)"
Cohesion: 0.15
Nodes (12): 1. Vue d'Ensemble des Modules et Schéma Textuel, 2.1 Flux de Données : Veille-Intel, 2.2 Flux de Données : Vibe-Audit, 2. Flux de Données (Data Flows), 3. Décisions d'Architecture (Architecture Decision Records - ADR), ADR-01 : Monorepo Python local piloté par `uv`, ADR-02 : Abandon des APIs LLM distantes au profit d'un moteur 100 % local et déterministe, ADR-03 : Persistance locale SQLite et stockage exclusif de texte brut (+4 more)

### Community 17 - "Stratégie de Test & Assurance Qualité"
Cohesion: 0.22
Nodes (8): 1. Niveaux de Test et Pyramide de Qualification, 2. Organisation des Fixtures de Test (`tests/fixtures/`), 3. Critères d'Acceptation par Exigence Fonctionnelle (`FR-xxx`), 4. Matrice des Cas Limites (Edge Cases) et Comportements Attendus, 5. Commandes d'Exécution des Tests, Stratégie de Test & Assurance Qualité, Volet Veille-Intel, Volet Vibe-Audit

### Community 18 - "common.sh"
Cohesion: 0.13
Nodes (29): check-prerequisites.sh script, check_dir(), check_file(), find_specify_root(), format_speckit_command(), get_current_branch(), get_feature_paths(), get_invoke_separator() (+21 more)

### Community 19 - "Stratégie Go-to-Marché & Prospection Manuelle B2B"
Cohesion: 0.10
Nodes (19): 1.1 Cible Volet 1 : Veille-Intel, 1.2 Cible Volet 2 : Vibe-Audit, 1. Cibles & Segments Prioritaires, 2. Canaux d'Acquisition & Sourcing des Contacts, 3. Quota Quotidien & Rythme d'Exécution, 4.1 Veille-Intel (Agences Marketing), 4.2 Vibe-Audit (Fondateurs d'Apps IA), 4. Scripts de Prospection Manuelle (+11 more)

### Community 20 - "Modélisation Financière, Calendrier d'Encaissement & Scénarios"
Cohesion: 0.11
Nodes (17): 1. Paramètres Fondamentaux & Taux de Change, 2.1 Pour le Plancher Financier (1 524,49 € / 1 000 000 FCFA), 2.2 Pour la Cible Financière (3 048,98 € / 2 000 000 FCFA), 2. Formule des Mensualités / Ventes Nécessaires, 3. Règle de Calendrier & Impact sur les Abonnements, 4.1 Atteinte du Plancher (1 000 000 FCFA / 1 525 €), 4.2 Atteinte de la Cible (2 000 000 FCFA / 3 049 €), 4. Calendrier de Signatures Requis pour Atteindre les Paliers (+9 more)

### Community 21 - "Cadre Juridique, Confidentialité des Données & Conformité Réglementaire"
Cohesion: 0.17
Nodes (11): 1.1 Conditions de Validité du Consentement, 1.2 Procédure d'Arrêt d'Urgence en Cas de Découverte de Données Réelles, 1. Protocole de Consentement Écrit Obligatoire (Vibe-Audit), 2.1 Base Légale : L'Intérêt Légitime, 2.2 Exercice Effectif du Droit d'Opposition, 2. Prospection Électronique B2B & Droit d'Opposition (RGPD), 3. Confidentialité & Protection des Données Clients, 4.1 Points à Vérifier auprès de la CNIL (+3 more)

### Community 22 - "Protocole de Consentement et d'Autorisation d'Audit Technique"
Cohesion: 0.22
Nodes (8): 1. Parties Prenantes, 2. Périmètre Technique Autorisé, 3. Fenêtre Temporelle d'Intervention, 4. Engagements Déontologiques et Limites Techniques, 5. Signature et Accord Formel, Le Client (Commanditaire), Le Prestataire (Auditeur), Protocole de Consentement et d'Autorisation d'Audit Technique

### Community 23 - "Tasks: [FEATURE NAME]"
Cohesion: 0.07
Nodes (26): Dependencies & Execution Order, Format: `[ID] [P?] [Story] Description`, Implementation for User Story 1, Implementation for User Story 2, Implementation for User Story 3, Implementation Strategy, Incremental Delivery, MVP First (User Story 1 Only) (+18 more)

### Community 24 - "speckit-analyze/SKILL.md"
Cohesion: 0.08
Nodes (25): 1. Initialize Analysis Context, 2. Load Artifacts (Progressive Disclosure), 3. Build Semantic Models, 4. Detection Passes (Token-Efficient Analysis), 5. Severity Assignment, 6. Produce Compact Analysis Report, 7. Provide Next Actions, 8. Offer Remediation (+17 more)

### Community 25 - "create_new_feature.py"
Cohesion: 0.16
Nodes (22): datetime, re, shlex, Args, _clean_branch_name(), _fit_branch_name(), _generate_branch_name(), _get_highest_from_specs() (+14 more)

### Community 26 - "Execution Steps"
Cohesion: 0.12
Nodes (15): 1. Initialize Convergence Context, 2. Load Artifacts (Progressive Disclosure), 3. Build the Intent Inventory, 4. Assess the Codebase and Classify Findings, 5. Assign Severity, 6. Present the In-Session Findings Summary, 7. Append Convergence Tasks (or report converged), 8. Provide Next Actions (Handoff) (+7 more)

### Community 27 - "Feature Specification: [FEATURE NAME]"
Cohesion: 0.15
Nodes (12): Assumptions, Edge Cases, Feature Specification: [FEATURE NAME], Functional Requirements, Key Entities *(include if feature involves data)*, Measurable Outcomes, Requirements *(mandatory)*, Success Criteria *(mandatory)* (+4 more)

### Community 28 - "speckit-plan/SKILL.md"
Cohesion: 0.18
Nodes (10): Completion Report, Done When, Key rules, Mandatory Post-Execution Hooks, Outline, Phase 0: Outline & Research, Phase 1: Design & Contracts, Phases (+2 more)

### Community 29 - "speckit-specify/SKILL.md"
Cohesion: 0.18
Nodes (10): Completion Report, Done When, For AI Generation, Mandatory Post-Execution Hooks, Outline, Pre-Execution Checks, Quick Guidelines, Section Requirements (+2 more)

### Community 30 - "speckit-tasks/SKILL.md"
Cohesion: 0.18
Nodes (10): Checklist Format (REQUIRED), Completion Report, Done When, Mandatory Post-Execution Hooks, Outline, Phase Structure, Pre-Execution Checks, Task Generation Rules (+2 more)

### Community 31 - "Core Principles"
Cohesion: 0.18
Nodes (10): Core Principles, Governance, [PRINCIPLE_1_NAME], [PRINCIPLE_2_NAME], [PRINCIPLE_3_NAME], [PRINCIPLE_4_NAME], [PRINCIPLE_5_NAME], [PROJECT_NAME] Constitution (+2 more)

### Community 32 - "Core Principles"
Cohesion: 0.18
Nodes (10): Core Principles, Governance, [PRINCIPLE_1_NAME], [PRINCIPLE_2_NAME], [PRINCIPLE_3_NAME], [PRINCIPLE_4_NAME], [PRINCIPLE_5_NAME], [PROJECT_NAME] Constitution (+2 more)

### Community 33 - "Implementation Plan: [FEATURE]"
Cohesion: 0.22
Nodes (8): Complexity Tracking, Constitution Check, Documentation (this feature), Implementation Plan: [FEATURE], Project Structure, Source Code (repository root), Summary, Technical Context

### Community 34 - "speckit-checklist/SKILL.md"
Cohesion: 0.25
Nodes (7): Anti-Examples: What NOT To Do, Checklist Purpose: "Unit Tests for English", Example Checklist Types & Sample Items, Execution Steps, Post-Execution Checks, Pre-Execution Checks, User Input

### Community 35 - "speckit-clarify/SKILL.md"
Cohesion: 0.29
Nodes (6): Completion Report, Done When, Mandatory Post-Execution Hooks, Outline, Pre-Execution Checks, User Input

### Community 36 - "speckit-implement/SKILL.md"
Cohesion: 0.29
Nodes (6): Completion Report, Done When, Mandatory Post-Execution Hooks, Outline, Pre-Execution Checks, User Input

### Community 37 - "speckit-constitution/SKILL.md"
Cohesion: 0.33
Nodes (5): Outline, Post-Execution Checks, Pre-Execution Checks, Scope Guard, User Input

### Community 38 - "speckit-taskstoissues/SKILL.md"
Cohesion: 0.40
Nodes (4): Outline, Post-Execution Checks, Pre-Execution Checks, User Input

### Community 39 - "[CHECKLIST TYPE] Checklist: [FEATURE NAME]"
Cohesion: 0.40
Nodes (4): [Category 1], [Category 2], [CHECKLIST TYPE] Checklist: [FEATURE NAME], Notes

## Knowledge Gaps
- **311 isolated node(s):** `common.sh script`, `1. Stack & Architecture`, `2. Resource Affinity (Auto-Routed)`, `3. Local Constraints & Conventions`, `Workspace Skills Index: veille-intel_vibe-audit` (+306 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 359 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `resolve_template_content()` connect `common.py` to `create_new_feature.py`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Why does `TemplateResolutionError` connect `common.py` to `create_new_feature.py`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `TemplateResolutionError` (e.g. with `main()` and `main()`) actually correct?**
  _`TemplateResolutionError` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `common.sh script`, `1. Stack & Architecture`, `2. Resource Affinity (Auto-Routed)` to the rest of the system?**
  _311 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Déroulement Pas à Pas` be split into smaller, more focused modules?**
  _Cohesion score 0.1111111111111111 - nodes in this community are weakly interconnected._
- **Should `1. Offre : Veille-Intel (Veille Concurrentielle Marque Blanche)` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `PRD Unifié : Veille-Intel & Vibe-Audit` be split into smaller, more focused modules?**
  _Cohesion score 0.06451612903225806 - nodes in this community are weakly interconnected._