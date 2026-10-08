# Architecture Technique du Système

---

## 1. Vue d'Ensemble des Modules et Schéma Textuel

Le projet est conçu comme un **monorepo Python 3.11+ local-first**, piloté par le gestionnaire d'environnement `uv`. Il héberge deux outils opérationnels distincts partageant une philosophie d'exécution 100 % locale, déterministe, sans dépendance d'API cloud payante ou externe.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MONOREPO PYTHON (uv)                               │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
         ┌────────────────────────────┴────────────────────────────┐
         ▼                                                         ▼
┌─────────────────────────────────┐       ┌───────────────────────────────────┐
│     MODULE 1 : VEILLE-INTEL     │       │      MODULE 2 : VIBE-AUDIT        │
│    (CLI: veille-intel)          │       │     (CLI: vibe-audit)             │
├─────────────────────────────────┤       ├───────────────────────────────────┤
│ 1. config_loader (YAML)         │       │ 1. consent_gate (consent/*.md)    │
│ 2. fetcher (httpx passif / 5s)  │       │ 2. scanner_secrets (regex/detect) │
│ 3. snapshots (SQLite local)     │       │ 3. scanner_sql_rls (sqlparse)     │
│ 4. differ (texte N vs N-1)      │       │ 4. scanner_deps (npm/pip audit)   │
│ 5. structurer (faits + dates)   │       │ 5. scanner_http (headers passifs) │
│ 6. renderer (Jinja2 / PDF/HTML) │       │ 6. remediation (prompts IA fix)   │
│                                 │       │ 7. reporter (PDF/HTML gravité)    │
└────────────────┬────────────────┘       └─────────────────┬─────────────────┘
                 │                                          │
                 ▼                                          ▼
     [ data/veille_intel.db ]                   [ data/vibe_audit.db ]
                 │                                          │
                 ▼                                          ▼
 [ export/<client>_S<semaine>.pdf ]          [ export/audit_<client>.pdf ]
```

---

## 2. Flux de Données (Data Flows)

### 2.1 Flux de Données : Veille-Intel

```
[ config/clients/<client>.yaml ]
             │
             ▼
      ( config_loader ) ──> Validation des 5 concurrents & URLs cibles
             │
             ▼
         ( fetcher )
             │  ├──> Vérification robots.txt (si Disallow : arrêt et tracé)
             │  ├──> Temporisation légale (1 requête / 5 secondes par domaine)
             │  └──> Requête GET passive (User-Agent honnête et transparent)
             │
             ▼
       ( snapshots ) ──> Extraction texte brut HTML (BeautifulSoup4)
             │           Archivage horodaté dans [ data/veille_intel.db ]
             ▼
        ( differ ) ──> Comparaison textuelle différentielle Semaine N vs N-1
             │         Si aucun delta : tracé explicite « Aucun changement »
             ▼
      ( structurer ) ──> Isolement des faits modifiés (tarifs, offres, dates)
             │           Production du brouillon structuré pour l'opérateur
             ▼
   [ Révision Humaine ] ──> L'opérateur valide les faits & ajuste les 3 actions
             │
             ▼
       ( renderer ) ──> Injection dans template Jinja2 marque blanche
             │
             ▼
[ export/<client>_S<N>.pdf ] ──> Livrable prêt à envoyer par email
```

### 2.2 Flux de Données : Vibe-Audit

```
[ Répertoire client : work/<client>/ ] + [ URL consentie ]
             │
             ▼
      ( consent_gate ) ──> Lecture de [ consent/<client>.md ]
             │             VÉRIFICATION BLOQUANTE :
             │             (Signataire présent ? Dates valides ? Périmètre OK ?)
             │             Si NON : ARRÊT IMMÉDIAT ET SORTIE CODE 1
             │             Si OUI : Autorisation accordée
             ▼
  ( Scanners Statiques )
             ├─> scanner_secrets  : Analyse code source + git log -p (masquage)
             ├─> scanner_sql_rls  : Analyse statique des migrations SQL Supabase
             ├─> scanner_deps     : Inspection statique npm audit & pip-audit
             └─> scanner_http     : Analyse passive en-têtes HTTP/TLS/CORS
             │
             ▼
    [ data/vibe_audit.db ] ──> Enregistrement des constats bruts horodatés
             │
             ▼
 [ Reproduction Humaine ] ──> L'opérateur reproduit manuellement chaque constat
             │                Si fausse alerte : écartée. Si preuve valide : retenue.
             ▼
      ( remediation ) ──> Attribution du niveau de gravité (Critique/Élevé/Moyen)
             │            Génération du prompt de correction adapté (Lovable/Bolt/Cursor)
             ▼
       ( reporter ) ──> Injection Jinja2 + Section obligatoire « Non testé »
             │
             ▼
[ export/audit_<client>.pdf ] ──> Rapport d'audit sous 48 h + Re-contrôle J+14
```

---

## 3. Décisions d'Architecture (Architecture Decision Records - ADR)

### ADR-01 : Monorepo Python local piloté par `uv`
- **Contexte :** Deux micro-services à livrables distincts, mais opérés par un développeur unique avec une exigence forte de zéro dépense et de simplicité d'exécution.
- **Décision :** Héberger les deux outils dans un unique dépôt Python structuré en sous-modules (`src/veille_intel` et `src/vibe_audit`), géré avec `uv` (exécutables `uv run veille-intel` et `uv run vibe-audit`).
- **Alternatives écartées :** 
  - Deux dépôts Git séparés : écarté pour éviter la duplication des configurations d'outils, des scripts de test et de la documentation transverse (`docs/`).
  - Architecture micro-services réseau avec API REST locale : écartée car sur-ingénierie inutile (ponytail-review) pour un usage en ligne de commande.
- **Conséquences :** Environnement d'exécution unifié, démarrage instantané avec `uv`, maintenance simplifiée des dépendances.

---

### ADR-02 : Abandon des APIs LLM distantes au profit d'un moteur 100 % local et déterministe
- **Contexte :** Le projet initial envisageait une API LLM cloud pour assister la synthèse des signaux et la rédaction des prompts de correction. Cependant, les risques de rupture de quota journalier, la dépendance réseau externe et la stricte confidentialité des données imposent une autonomie totale.
- **Décision :** Aucun appel LLM dans le code applicatif. Le système repose sur :
  1. Un calcul différentiel textuel rigoureux et déterministe (diff ligne par ligne et extraction de blocs modifiés).
  2. Des gabarits paramétrés pour structurer les signaux et les prompts de correction.
  3. La revue et l'éditorialisation finale assurées par l'opérateur humain (humain dans la boucle).
- **Alternatives écartées :**
  - Maintien d'APIs LLM cloud gratuites : écarté pour éliminer tout risque d'indisponibilité, de latence réseau et d'éventuelles hallucinations de faits.
  - Modèle LLM local exécuté par Ollama : écarté en raison des contraintes de mémoire et de CPU sur la machine locale sans GPU dédié garanti.
- **Conséquences :** 100 % reproductible, zéro dépendance réseau externe pour le traitement, zéro clé d'API requise, confidentialité absolue et conformité parfaite au principe de zéro dépense.

---

### ADR-03 : Persistance locale SQLite et stockage exclusif de texte brut
- **Contexte :** Veille-Intel doit comparer l'état d'une page publique entre la semaine N et la semaine N-1. Vibe-Audit doit enregistrer les constats validés.
- **Décision :** Utiliser SQLite (`data/veille_intel.db` et `data/vibe_audit.db`). Pour la veille, stocker uniquement le texte brut extrait (nettoyé des balises HTML, scripts et styles via BeautifulSoup4) horodaté avec l'URL source.
- **Alternatives écartées :**
  - Stockage des pages HTML complètes ou captures d'écran : écarté pour éviter l'explosion de l'espace disque et les diffs pollués par les tokens dynamiques ou styles CSS.
  - Base de données serveur distante (PostgreSQL) : écartée car viole le principe de zéro dépense et de simplicité locale.
- **Conséquences :** Base de données compacte (< 50 Mo pour 5 concurrents sur plusieurs mois), requêtes SQL rapides, sauvegarde triviale par simple copie de fichier.

---

### ADR-04 : Sas de consentement technique bloquant (`consent_gate`)
- **Contexte :** Vibe-Audit analyse du code tiers et inspecte des URLs publiques. L'analyse sans consentement écrit formel est illégale (art. 323-1 du Code pénal) et viole les garde-fous fondamentaux du projet.
- **Décision :** Implémenter un module `consent_gate` qui vérifie obligatoirement avant toute action l'existence, la non-vacuité et la validité temporelle du fichier Markdown `consent/<client_id>.md`. Si le fichier est manquant ou non conforme, la CLI interrompt immédiatement l'exécution avec un code de sortie d'erreur (`exit 1`) sans exécuter le moindre contrôle.
- **Alternatives écartées :**
  - Simple avertissement textuel dans la console sans blocage : écarté pour risque juridique inacceptable.
  - Validation manuelle sans contrôle logiciel : écartée pour garantir la preuve d'audit opposable.
- **Conséquences :** Impossibilité technique absolue d'exécuter un audit sur une cible non consentie.

---

### ADR-05 : Rendu documentaire Jinja2 avec double cible (WeasyPrint et HTML autonome)
- **Contexte :** Les agences exigent un PDF de haute qualité, 100 % marque blanche. Cependant, les moteurs PDF en Python dépendent parfois de bibliothèques système C (`libpango`, `libcairo`) susceptibles de manquer sur certains environnements Linux.
- **Décision :** Concevoir les gabarits en HTML/CSS soigné via Jinja2. Le module de rendu tente une compilation directe en PDF via WeasyPrint. Si les bibliothèques C ne sont pas installées, le système génère un fichier HTML autonome propre et ouvre le navigateur pour permettre l'export PDF natif en 2 clics via « Imprimer en PDF ».
- **Alternatives écartées :**
  - Bibliothèques payantes ou services d'API de conversion PDF cloud : écartés (Garde-fou #2).
  - Génération PDF brute via ReportLab : écartée pour complexité de mise en page et maintenance fastidieuse par rapport à du HTML/CSS.
- **Conséquences :** Robustesse absolue sur tout environnement, mise en page responsive et élégante, zéro dépendance payante.

---

### ADR-06 : Inspection statique des dépendances sans exécution de `npm install`
- **Contexte :** Vibe-Audit doit auditer les dépendances de projets créés avec Lovable ou Bolt. Exécuter un `npm install` sur du code client inconnu présente un risque de sécurité majeur (exécution de scripts de pré/post-installation malveillants).
- **Décision :** Analyser uniquement les fichiers statiques de verrouillage (`package-lock.json`, `pnpm-lock.yaml`, `requirements.txt`). Utiliser `npm audit --package-lock-only` ou des parseurs directs de manifests sans jamais exécuter d'installation dynamique de paquets.
- **Alternatives écartées :**
  - Cloner et installer l'ensemble des dépendances localement : écarté pour risque de compromission de l'environnement opérateur.
- **Conséquences :** Sécurité totale de l'environnement de travail de Kreesten, audit ultra-rapide (< 10 secondes par analyse de dépendances).
