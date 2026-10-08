# Stratégie de Test & Assurance Qualité

> **Règle absolue (Garde-fous #5 et #7) :** Tous les tests s'exécutent hors-ligne sans dépendance réseau requise. Fixtures de test 100 % fictives, aucun secret ni donnée client réelle dans git. Tests automatisés obligatoires avant de marquer tout lot comme terminé.

---

## 1. Niveaux de Test et Pyramide de Qualification

```
                     ┌─────────────────────────────┐
                     │     TESTS DE BOUT EN BOUT   │  Scénarios complets sur
                     │          (E2E CLI)          │  fixtures fictives hors-ligne
                     └──────────────┬──────────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │    TESTS D'INTÉGRATION      │  Chaîne locale : DB SQLite,
                     │     (Composants couplés)    │  diff, gabarits Jinja2
                     └──────────────┬──────────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │      TESTS UNITAIRES        │  Fonctions pures, regex,
                     │          (pytest)           │  parsing SQL, calculs de diff
                     └─────────────────────────────┘
```

1. **Tests Unitaires (`tests/unit/`) :** Vérifient les règles métiers, expressions régulières de secrets, parseurs de configuration et logique de calcul différentiel en isolation totale. Exécution instantanée (< 2 secondes).
2. **Tests d'Intégration (`tests/integration/`) :** Valident la persistance SQLite, les transactions de snapshots, l'injection des gabarits Jinja2 et les mécanismes de sas de sécurité (`consent_gate`).
3. **Tests de Bout en Bout (`tests/e2e/`) :** Simulent l'appel des commandes en ligne de commande `veille-intel` et `vibe-audit` sur une fausse cible de veille (fichiers HTML statiques servis localement ou mockés) et un faux projet applicatif volontairement vulnérable.

---

## 2. Organisation des Fixtures de Test (`tests/fixtures/`)

Les fixtures sont strictement fictives, anonymisées et intégrées au dépôt pour garantir la reproductibilité des tests sans connexion internet :

| Répertoire de Fixture | Description & Contenu |
| :--- | :--- |
| `tests/fixtures/configs/` | Fichiers YAML valides (`client_valide.yaml`) et invalides (URLs manquantes, > 5 concurrents, syntaxe corrompue). |
| `tests/fixtures/html/` | Instantanés HTML de pages web enregistrées hors-ligne : semaine N (`pricing_v1.html`) et semaine N+1 avec changements (`pricing_v2.html`), pages vides, pages sans balises exploitables. |
| `tests/fixtures/consent/` | Fichiers de consentement : valide (`consent_ok.md`), périmé (`consent_expired.md`), sans signataire (`consent_no_signer.md`), et répertoire vide. |
| `tests/fixtures/vulnerable_app/` | Faux dépôt d'application web fictive contenant des vulnérabilités de test connues : faux token OpenAI (`sk-TEST12345...`), faux secret Stripe (`sk_test_...`), table SQL sans RLS, et fausse clé client dans le bundle JS. |
| `tests/fixtures/sql/` | Scripts SQL de migrations Supabase : migrations sécurisées (avec `ENABLE ROW LEVEL SECURITY`) et vulnérables (avec `USING (true)` ou sans RLS). |

---

## 3. Critères d'Acceptation par Exigence Fonctionnelle (`FR-xxx`)

### Volet Veille-Intel

| Réf. Exigence | Description de l'Exigence | Critère d'Acceptation & Scénario de Test Validant | Type de Test |
| :--- | :--- | :--- | :---: |
| **FR-001** | Chargement de la configuration client YAML. | Le système valide la présence du client, parse jusqu'à 5 URLs concurrentes et lève une exception explicite si le fichier est manquant ou invalide. | Unitaire |
| **FR-002** | Respect impératif du `robots.txt`. | Mock d'un `robots.txt` interdisant `/pricing`. Le fetcher refuse d'extraire la page, consigne la cause dans les logs et retourne un statut d'exclusion. | Unitaire |
| **FR-003** | Temporisation 5s et User-Agent honnête. | Vérification de l'intervalle d'horodatage entre requêtes sur un même domaine ($\ge 5,0\text{ s}$) et inspection de l'en-tête `User-Agent`. | Intégration |
| **FR-004** | Archivage SQLite du texte brut horodaté. | Le texte HTML brut est nettoyé des balises scripts/styles et sauvegardé dans `veille_intel.db` avec URL et horodatage UTC vérifiables. | Intégration |
| **FR-005** | Différentiel N vs N-1 & gestion du statut vide. | En comparant `pricing_v1.html` et `pricing_v2.html`, le delta textuel est extrait. Si les deux versions sont identiques, le système génère « Aucun changement observé ». | Unitaire |
| **FR-006** | Séparation faits / dates / recommandations. | Chaque signal produit dans le canevas comporte l'URL source, la date de capture, la citation textuelle brute du changement et un emplacement pour 3 actions. | Unitaire |
| **FR-007** | Moteur de rendu PDF/HTML marque blanche. | Le document généré ne comporte aucune mention de `veille-intel` ni de marque technique. Rendu conforme de 3 à 6 pages avec mise en page soignée. | E2E |
| **FR-008** | Génération déterministe locale sans LLM. | Le pipeline d'extraction s'exécute à 100 % hors-ligne sans clé d'API, sans appel réseau tiers et sans dépendance externe. | Unitaire |
| **FR-009** | Fetcher Playwright conditionnel. | Activé uniquement via le flag `--browser` ; le mode par défaut demeure `httpx`. | Intégration |

### Volet Vibe-Audit

| Réf. Exigence | Description de l'Exigence | Critère d'Acceptation & Scénario de Test Validant | Type de Test |
| :--- | :--- | :--- | :---: |
| **FR-010** | Sas de consentement technique bloquant. | Si le fichier `consent/<client>.md` est absent, vide ou périmé, la CLI s'interrompt immédiatement avec code de retour `1` et refuse d'analyser la cible. | Unitaire & E2E |
| **FR-011** | Détection et masquage de secrets. | Détecte les faux secrets dans le code et dans l'historique git. Les valeurs affichées dans les constats sont systématiquement masquées (ex. `sk-TE****`). | Unitaire |
| **FR-012** | Détection des failles SQL / RLS Supabase. | Analyse statique d'un fichier `.sql` contenant `CREATE TABLE ...` sans `ENABLE ROW LEVEL SECURITY` : la table est signalée comme faille critique. | Unitaire |
| **FR-013** | Détection de clés d'API exposées frontend. | Détecte la présence de clés `service_role` ou de clés privées dans des fichiers JS/TS publics ou `.env.production`. | Unitaire |
| **FR-014** | Audit statique des dépendances (lockfiles). | Analyse `package-lock.json` via `npm audit` sans jamais appeler `npm install`. Remonte les CVE connues sur les paquets fictifs de test. | Intégration |
| **FR-015** | Inspection passive des en-têtes HTTP de sécurité. | Relève l'absence de CSP, HSTS, X-Content-Type-Options et les politiques CORS trop permissives (`*`) sans injection active. | Intégration |
| **FR-016** | Génération de prompts de remédiation ciblés. | Pour chaque faille identifiée, le rapport intègre le niveau de gravité (Critique, Élevé, Moyen, Faible), l'impact et le prompt exact prêt à copier pour Lovable/Bolt. | Unitaire |
| **FR-017** | Mention obligatoire des périmètres non testés. | Le rapport généré comporte une section expresse et standardisée énumérant les éléments non testés (pas d'intrusion active, pas d'audit mobile, etc.). | Unitaire |

---

## 4. Matrice des Cas Limites (Edge Cases) et Comportements Attendus

| Cas Limite (Edge Case) | Module Concerné | Comportement Attendu du Système | Validation de Test |
| :--- | :--- | :--- | :--- |
| **Page web vide (0 octet)** | `veille_intel.fetcher` | Levée d'un avertissement sans crash. Tracé dans la base : « Contenu vide lors de la capture ». Aucun faux signal généré. | `test_fetcher_empty_page()` |
| **Erreur HTTP 403 / 404 / 429** | `veille_intel.fetcher` | Enregistrement de l'incident avec le code HTTP. Notification dans le rapport : « Source temporairement indisponible le [Date] ». Aucun contournement tenté. | `test_fetcher_http_errors()` |
| **Absence de modifications (N = N-1)** | `veille_intel.differ` | Génération explicite de l'entrée « Aucune modification observée pour le concurrent X cette semaine ». | `test_differ_no_changes()` |
| **Fichier de consentement absent** | `vibe_audit.consent` | Arrêt immédiat (`exit 1`) avec message d'erreur : `ERREUR : Consentement écrit obligatoire manquant (consent/<client>.md)`. Aucun scan exécuté. | `test_consent_gate_missing()` |
| **Consentement avec date expirée** | `vibe_audit.consent` | Arrêt immédiat (`exit 1`) avec message d'erreur : `ERREUR : La date d'autorisation est échue`. | `test_consent_gate_expired()` |
| **Fichier SQL de migration corrompu** | `vibe_audit.sql_scanner` | Gestion sécurisée de l'exception de parsing, signalement du fichier non analysable dans la section « Non testé » sans planter la suite de l'audit. | `test_sql_scanner_malformed()` |
| **Absence de dépendances graphiques C** | `renderer` | Bascule automatique et transparente vers l'export HTML autonome imprimable sans lever d'exception non gérée. | `test_renderer_fallback_html()` |
| **Mode hors-ligne total (pas d'Internet)** | Suite complète | 100 % de la suite de tests `pytest` s'exécute avec succès en mode avion / déconnecté. | `pytest tests/` (hors-ligne) |

---

## 5. Commandes d'Exécution des Tests

Toutes les commandes s'exécutent via `uv` dans l'environnement virtuel local :

```bash
# Exécution de l'intégralité de la suite de tests unitaires et d'intégration
uv run pytest tests/ -v

# Exécution avec mesure de couverture de code
uv run pytest --cov=src tests/

# Vérification spécifique du sas de consentement (sécurité bloquante)
uv run pytest tests/unit/test_consent_gate.py -v

# Vérification spécifique du moteur différentiel (intégrité des signaux)
uv run pytest tests/unit/test_differ.py -v
```
