# Boîte à Outils Autorisée et Liste Fermée (Outils Retenus & Écartés)

> **Règle absolue (Garde-fous #2 et #8) :** Zéro dépense, aucune inscription payante, aucune saisie de carte bancaire. Seuls les outils marqués **RETENU** dans ce document sont autorisés à l'exécution. Tout outil marqué **ÉCARTÉ** est formellement interdit. Tout élément non confirmé par une source officielle est marqué **À VÉRIFIER**.

---

## 1. Inventaire et Évaluation des Outils Candidats

| Outil | Rôle dans le projet | Gratuit & Limites vérifiées (Source) | Licence | Risque légal / ToS / Tokens | Décision |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **`httpx` + `BeautifulSoup4`** | Pages statiques, outil par défaut. Utilisé par scripts/capture.py pour toutes les captures de pages de clients (Veille-Intel). | 100 % gratuit, local, exécution illimitée. | BSD-3-Clause (`httpx`) / MIT (`beautifulsoup4`). | Collecte statique locale respectant robots.txt et 5 secondes de délai par domaine. | **RETENU** |
| **Playwright standard** | Pages publiques qui exigent du JavaScript, à utiliser dès que httpx renvoie un contenu vide. | Open source, 0 €. [playwright.dev, oct. 2026]. | Apache-2.0. | Rendu JS public respectant robots.txt, délai de 5 s, sans contournement anti-bot. | **RETENU** |
| **Firecrawl (MCP)** | Recherche publique, repérage de prospects et rapports d'échantillon uniquement. | non vérifié. Arrêt dès épuisement des crédits gratuits, zéro carte bancaire. | Propriétaire commercial. | Recherche publique et prospects uniquement. Jamais sur les données d'un client (NFR-002). | **RETENU** |
| **Agent-Reach** | Lecture de contenus publics de réseaux sociaux pour repérer des prospects (lancements de fondateurs, agences). | non vérifié (accès public sans frais d'API). | non vérifié. | Contenu public uniquement, aucun compte, aucun contournement, aucun envoi de message (garde-fou n°4). | **RETENU** |
| **Scanner de secrets Python interne** | Moteur déterministe local regex (clés OpenAI, Supabase `service_role`, Stripe, GitHub) + `git log -p`. | 100 % gratuit, code interne du projet, local. | MIT / Apache-2.0. | Analyse regex 100 % locale sans fuite de secrets ni transmission réseau. | **RETENU** |
| **`detect-secrets`** (Yelp) via `uvx` | Filtre complémentaire d'analyse statique de secrets et d'entropie dans le code et les commits (Vibe-Audit). | 100 % gratuit, exécution locale sans compte ni réseau (v1.5.0 vérifié). | Apache-2.0 (Open Source, usage commercial libre). | Scan statique local des dépôts et commits sans aucune donnée sortante. | **RETENU** |
| **`npm audit`** | Audit statique des dépendances JavaScript / TypeScript déclarées dans `package-lock.json` (Vibe-Audit). | 100 % gratuit, intégré nativement à Node.js / npm (v10.9.9 installé). | Artistic License 2.0 (Usage commercial permis). | Inspection statique du package-lock.json sans exécuter npm install sur la machine. | **RETENU** |
| **`pip-audit`** (Trail of Bits / PyPA) via `uvx` | Audit statique des dépendances Python déclarées dans `requirements.txt` ou `pyproject.toml` (Vibe-Audit). | 100 % gratuit, exécution locale éphémère (v2.10.1 vérifié). | Apache-2.0 (Usage commercial libre). | Audit local des manifestes Python via consultation sécurisée des vulnérabilités connues. | **RETENU** |
| **Parser SQL interne (`sqlparse`)** | Analyse syntaxique locale des migrations et scripts SQL pour détecter l'absence de RLS Supabase (Vibe-Audit). | 100 % gratuit, bibliothèque Python locale pure. | BSD-3-Clause. | Analyse syntaxique locale des migrations SQL sans aucune connexion réseau. | **RETENU** |
| **Jinja2 + WeasyPrint / HTML statique** | Moteur de rendu des rapports (Veille et Audit). Export PDF WeasyPrint avec repli natif HTML imprimable. | 100 % gratuit, open-source local. Repli direct vers HTML propre imprimable en PDF. | BSD-3-Clause (`jinja2`) / BSD-3-Clause (`weasyprint`). | Génération locale de rapports sans dépendance réseau avec repli HTML soigné. | **RETENU** |
| **`graphify`** (CLI locale) | Cartographie des relations du projet et visualisation des dépendances documentaires. | 100 % gratuit en mode code/doc local (`graphify update .`), 0 token LLM consommé. | Apache-2.0 / MIT. | Cartographie locale du code et de la documentation sans aucun appel LLM. | **RETENU** |
| **Context7 (MCP & Skills)** | Recherche de documentation officielle et versionnée des bibliothèques (`httpx`, `pytest`, etc.). | Gratuit, serveur MCP actif (`mcp.context7.com`). | Service gratuit développeur. | Consultation ponctuelle de documentation officielle pour valider la syntaxe du code. | **RETENU** |
| **GitHub MCP Server** | Gestion locale et distante des branches, commits et tickets git. | Inclus avec l'environnement Antigravity, gratuit. | MIT. | Gestion locale et distante des commits et tickets via authentification sécurisée. | **RETENU** |
| **Notion & Obsidian (MCP)** | Documentation interne, notes de méthode et suivi du projet. | Gratuit (accès local Obsidian / API Notion standard). | Propriétaire. | Notes méthodologiques uniquement ; aucune donnée client, aucune donnée personnelle de prospect (NFR-002). | **RETENU** |
| **SpecKit (`/speckit-*`)** | Suite de cadrage formel, spécifications techniques et décomposition des tâches. | 100 % gratuit, templates et dossiers locaux (.specify/ existe et configuré). | MIT / Open Source. | Spécification et cadrage formels du projet via les artefacts du dossier .specify/. | **RETENU** |
| **Brag** | Génération de courtes vidéos de démonstration pour valoriser les livrables d'audit. | non vérifié. | non vérifié. | Génération locale de courtes vidéos de démonstration pour illustrer les audits. | **RETENU** |
| **Astryx** | Outil non identifié dans l'environnement local. | non vérifié. | non vérifié. | Outil non identifié dans l'environnement local. Ne pas utiliser avant vérification. | non vérifié, ne pas utiliser avant vérification |

### Scraping : choix final

Le dispositif de collecte et scraping repose sur quatre outils retenus et strictement encadrés :
- **`httpx` + `BeautifulSoup4`** : Outil par défaut pour la capture passive de pages publiques statiques de clients (utilisé par `scripts/capture.py` dans Veille-Intel).
- **Playwright standard** : Navigateur headless pour le rendu de pages publiques exigeant du JavaScript, dès que `httpx` renvoie un contenu vide.
- **Firecrawl (MCP)** : Utilisé exclusivement pour la recherche publique, le repérage de prospects et la production de rapports d'échantillon. Arrêt impératif dès épuisement des crédits gratuits, zéro carte bancaire, et interdiction formelle de lui transmettre les URLs ou la liste de concurrents d'un client (confidentialité NFR-002).
- **Agent-Reach** : Utilisé uniquement pour la lecture de publications publiques sur les réseaux sociaux (lancements de fondateurs, agences) afin d'identifier des prospects. Contenu public uniquement, sans compte ni contournement, et jamais utilisé pour envoyer des messages (garde-fou n°4).

> **Règle absolue :** Le respect strict de `robots.txt`, le délai d'au moins 5 secondes entre deux requêtes vers un même domaine et l'absence totale de contournement (anti-bot, login, CAPTCHA) s'appliquent rigoureusement à `httpx` et à Playwright.

---

## Outil par Tâche

| Tâche | Outil retenu |
| :--- | :--- |
| Capture de pages statiques de clients | `httpx` + `BeautifulSoup4` |
| Capture de pages JS | Playwright standard |
| Recherche et repérage de prospects | Firecrawl (MCP) et Agent-Reach |
| Analyse des secrets | Scanner de secrets interne et `detect-secrets` |
| Analyse SQL / RLS | Parser SQL interne (`sqlparse`) |
| Audit des dépendances | `npm audit` et `pip-audit` |
| Rendu des rapports | Jinja2 + WeasyPrint / HTML statique |
| Spécifications | SpecKit (`/speckit-*`) |
| Notes de suivi | Notion & Obsidian (MCP) |
| Vidéo de démonstration | Brag |
| Gestion git | GitHub MCP Server |

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
2. **Aucun appel LLM dans le code applicatif (décision conservée). L'analyse et les recommandations sont rédigées par l'opérateur.**
3. **Double niveau pour les secrets :** Scanner regex interne Python (dédié aux tokens connus : `sk-...`, `service_role`, Stripe) complété par `uvx detect-secrets`.
4. **Liste des outils révisée et validée par l'opérateur le 8 octobre 2026.**
5. **Firecrawl et Agent-Reach : recherche de prospects et échantillons uniquement, jamais sur les données d'un client.**
6. **Volume des snapshots :** Seul le texte brut extrait des pages publiques est archivé dans SQLite (`veille_intel.db`), garantissant une taille de base inférieure à 50 Mo.
7. **Précaution `npm audit` :** Analyse statique exclusive de `package.json` et `package-lock.json` sans jamais exécuter `npm install`.
