# Boîte à Outils Autorisée et Liste Fermée (Outils Retenus & Écartés)

> **Règle absolue (Garde-fous #2 et #8) :** Zéro dépense, aucune inscription payante, aucune saisie de carte bancaire. Seuls les outils marqués **RETENU** dans ce document sont autorisés à l'exécution. Tout outil marqué **ÉCARTÉ** est formellement interdit. Tout élément non confirmé par une source officielle est marqué **À VÉRIFIER**.

---

## 1. Inventaire et Évaluation des Outils Candidats

| Outil | Rôle dans le projet | Gratuit & Limites vérifiées (Source) | Licence | Risque légal / ToS / Tokens | Décision |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **`httpx` + `BeautifulSoup4`** | Collecte HTTP passive, extraction de texte public et vérification `robots.txt` (Veille-Intel). | 100 % gratuit, local, exécution illimitée. | BSD-3-Clause (`httpx`) / MIT (`beautifulsoup4`). | **Nul.** Aucun risque anti-bot, respect strict de 1 req/5s et `robots.txt`. Faible empreinte. | **RETENU** |
| **Scanner de secrets Python interne** | Moteur déterministe local regex (clés OpenAI, Supabase `service_role`, Stripe, GitHub) + `git log -p`. | 100 % gratuit, code interne du projet, local. | MIT / Apache-2.0. | **Nul.** Analyse 100 % locale, aucune donnée sortante, masquage immédiat des valeurs. | **RETENU** |
| **`detect-secrets`** (Yelp) via `uvx` | Filtre complémentaire d'analyse statique de secrets et d'entropie dans le code et les commits (Vibe-Audit). | 100 % gratuit, exécution locale sans compte ni réseau (v1.5.0 vérifié). | Apache-2.0 (Open Source, usage commercial libre). | **Nul.** Analyse 100 % locale sans transmission de données. | **RETENU** |
| **`npm audit`** | Audit statique des dépendances JavaScript / TypeScript déclarées dans `package-lock.json` (Vibe-Audit). | 100 % gratuit, intégré nativement à Node.js / npm (v10.9.9 installé). | Artistic License 2.0 (Usage commercial permis). | **Très faible.** Exécution statique sur le lockfile sans `npm install`. | **RETENU** |
| **`pip-audit`** (Trail of Bits / PyPA) via `uvx` | Audit statique des dépendances Python déclarées dans `requirements.txt` ou `pyproject.toml` (Vibe-Audit). | 100 % gratuit, exécution locale éphémère (v2.10.1 vérifié). | Apache-2.0 (Usage commercial libre). | **Très faible.** Consultation de l'API publique OSV/PyPI pour les advisories connus. | **RETENU** |
| **Parser SQL interne (`sqlparse`)** | Analyse syntaxique locale des migrations et scripts SQL pour détecter l'absence de RLS Supabase (Vibe-Audit). | 100 % gratuit, bibliothèque Python locale pure. | BSD-3-Clause. | **Nul.** Analyse statique locale sans connexion à une base distante. | **RETENU** |
| **Jinja2 + WeasyPrint / HTML statique** | Moteur de rendu des rapports (Veille et Audit). Export PDF WeasyPrint avec repli natif HTML imprimable. | 100 % gratuit, open-source local. Repli direct vers HTML propre imprimable en PDF. | BSD-3-Clause (`jinja2`) / BSD-3-Clause (`weasyprint`). | **Nul.** Autonomie totale, indépendant des dépendances C complexes. | **RETENU** |
| **`graphify`** (CLI locale) | Cartographie des relations du projet et visualisation des dépendances documentaires. | 100 % gratuit en mode code/doc local (`graphify update .`), 0 token LLM consommé. | Apache-2.0 / MIT. | **Nul.** Exécution purement locale sans extraction sémantique externe. | **RETENU** (Mode code seul) |
| **Context7 (MCP & Skills)** | Recherche de documentation officielle et versionnée des bibliothèques (`httpx`, `pytest`, etc.). | Gratuit, serveur MCP actif (`mcp.context7.com`). | Service gratuit développeur. | **Faible.** Consommation mesurée de contexte pour valider la syntaxe des dépendances. | **RETENU** |
| **GitHub MCP Server** | Gestion locale et distante des branches, commits et tickets git. | Inclus avec l'environnement Antigravity, gratuit. | MIT. | **Faible.** Authentification par token existant, aucun envoi de secrets. | **RETENU** |
| **Playwright standard** | Rendu headless de pages publiques nécessitant impérativement du JavaScript (Veille-Intel). | Open source, 0 €. [playwright.dev, oct. 2026]. | Apache-2.0. | **Faible.** Utilisé uniquement en dernier recours si `httpx` échoue sur une page publique JS. | **RETENU** (Conditionnel) |
| **Google Gemini API** | Connecteur externe d'appel LLM. | Palier gratuit (1 500 RPD). | Conditions d'utilisation Google AI Studio. | **Supprimé par décision utilisateur.** Remplacé par une logique 100 % locale et déterministe. | **ÉCARTÉ** |
| **Invisible-Playwright (MCP)** | Navigateur headless avec évasion anti-bot (`INVPW_TRUE_HEADLESS=1`). | Gratuit dans l'environnement. | Inconnue. | **ÉLEVÉ.** Viole expressément le Garde-fou #3 (anti-bot interdit). | **ÉCARTÉ** |
| **Google Maps Scraper** | Extraction de données massives sur Google Maps. | Gratuit local Docker. | Open Source. | **ÉLEVÉ.** Risque de violation des ToS Google et hors périmètre du projet. | **ÉCARTÉ** |
| **Sales Outreach Automation** | Envoi automatique d'emails de prospection en masse. | Inconnu. | Inconnue. | **CRITIQUE.** Viole le Garde-fou #4 (aucun envoi automatique de messages, l'humain envoie). | **ÉCARTÉ** |
| **Firecrawl (MCP)** | Moteur de crawl et de scraping web via service cloud. | 500 crédits d'amorce gratuits, puis offre payante par carte bancaire. | Propriétaire commercial. | **Moyen.** Risque de blocage ou d'exigence de carte bancaire à l'épuisement des crédits. | **ÉCARTÉ** (`httpx` prioritaire) |
| **Scrapling** | Scraping avec contournement de protections anti-bot (Cloudflare Turnstile). | Open source. | Inconnue. | **ÉLEVÉ.** Risque de confusion avec les modes de contournement anti-bot interdits. | **ÉCARTÉ** |
| **Agent-Reach** | Lecture de contenus sur 16 réseaux sociaux (Twitter, LinkedIn, Reddit, YouTube). | Gratuit sans clé d'API. | Inconnue. | **Moyen.** Hors périmètre pour Veille-Intel (sites d'entreprises) ; instabilité des scrapers sociaux. | **ÉCARTÉ** |
| **ScrapeGraphAI** | Scraping guidé par LLM envoyant des pages complètes à des modèles. | Open source, mais coût tokens externe. | MIT. | **ÉLEVÉ.** Consommation massive de tokens incompatible avec le coût zéro. | **ÉCARTÉ** |
| **Notion & Obsidian (MCP)** | Synchronisation cloud de notes et bases de données. | Notion MCP actif / Obsidian MCP désactivé. | Propriétaire. | **Moyen.** Inutile pour un opérateur solo. Stockage local SQLite/CSV beaucoup plus rapide. | **ÉCARTÉ** |
| **LinkedIn Ghostwriting** | Génération de publications LinkedIn B2B. | Gratuit local. | Inconnue. | **Faible.** Hors périmètre (prospection manuelle ciblée 1-à-1 par email uniquement). | **ÉCARTÉ** |
| **MiroFish, Rea, Astryx** | Outils candidats non répertoriés. | Inexistants sur l'environnement. | Inconnue. | **N/A.** Non identifiables ou expressément exclus. | **ÉCARTÉ** |
| **SpecKit (`/speckit-*`)** | Suite de commandes de spécification formelle. | Non installé dans le système. | Inconnue. | **N/A.** Démarche appliquée manuellement via des fichiers Markdown standardisés. | **À VÉRIFIER** (Non installé) |
| **BrightData Plugin Search** | Recherche web via proxy résidentiel BrightData. | Non configuré / non présent. | Commercial. | **Moyen.** Dépendance externe superflue. | **ÉCARTÉ** |
| **Brag** | Générateur de vidéo de démonstration. | Non présent. | Inconnue. | **Faible.** Différé à plus tard si besoin de supports visuels marketing. | **ÉCARTÉ** |

---

## 2. Skills à Invoquer par Tâche (8 Skills Actifs au Maximum)

Conformément à la règle n° 8 des garde-fous, chaque skill est référencé par son nom exact avec le préfixe `/` :

| Tâche | Skill (Nom exact avec `/`) | Quand l'invoquer |
| :--- | :--- | :--- |
| **1. Cartographie du projet** | `/graphify` | À chaque mise à jour de la documentation ou ajout d'un module pour vérifier la cohérence du graphe (mode code pur). |
| **2. Documentation des APIs & Libs** | `/context7` | Avant d'écrire ou de modifier du code utilisant des bibliothèques externes (`httpx`, `jinja2`, `pytest`) pour vérifier la syntaxe exacte. |
| **3. Analyse SQL & Sécurité RLS** | `/sql-analyst` | Pendant la conception du scanner de politiques Supabase et l'évaluation des fichiers de migrations SQL dans Vibe-Audit. |
| **4. Hygiène rédactionnelle & Ton** | `/antislop` | Lors de la rédaction ou de la révision des rapports finaux, des scripts de prospection et de la documentation client (zéro jargon IA). |
| **5. Simplification & Anti-sur-ingénierie** | `/ponytail-review` | Lors de chaque revue de code avant commit pour traquer les abstractions inutiles et maintenir le code le plus minimal possible. |
| **6. Développement piloté par les tests** | `/python-testing` | Lors de l'écriture des tests unitaires et d'intégration `pytest` avec fixtures offline avant de considérer un lot comme terminé. |
| **7. Contrôles de sécurité applicative** | `/security-best-practices` | Lors du développement et de la validation des règles de détection de vulnérabilités pour Vibe-Audit (CORS, secrets, RLS). |
| **8. Rendu web complexe (si requis)** | `/playwright` | Uniquement lorsqu'une page publique cible de Veille-Intel requiert du rendu JavaScript et que `httpx` ne peut pas extraire le contenu. |

---

## 3. Décisions Opérateur & Arbitrages Validés

1. **Rendu PDF :** Option de repli validée. En cas d'indisponibilité des dépendances C de WeasyPrint, le système génère un fichier HTML/CSS soigné directement imprimable en PDF via le navigateur.
2. **Suppression de l'API Gemini :** Validée. Aucune API LLM externe n'est intégrée dans le code applicatif. Le traitement repose sur une logique 100 % locale et déterministe (différentiel textuel, règles de détection précises, gabarits paramétrés). L'analyse stratégique humaine et les prompts de correction sont générés sans appel d'API payant ou dépendant.
3. **Double niveau pour les secrets :** Scanner regex interne Python (dédié aux tokens connus : `sk-...`, `service_role`, Stripe) complété par `uvx detect-secrets`.
4. **Volume des snapshots :** Seul le texte brut extrait des pages publiques est archivé dans SQLite (`veille_intel.db`), garantissant une taille de base inférieure à 50 Mo.
5. **Précaution `npm audit` :** Analyse statique exclusive de `package.json` et `package-lock.json` sans jamais exécuter `npm install`.
