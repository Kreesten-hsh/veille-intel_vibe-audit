# Spécification des Offres Commerciales

---

## 1. Offre : Veille-Intel (Veille Concurrentielle Marque Blanche)

### Contexte & Problème
Les agences marketing françaises souhaitent enrichir leur offre avec un service récurrent de veille stratégique pour leurs clients PME/ETI, mais ne disposent pas du budget ni du volume pour recruter un analyste à temps plein.

### Cible
- Dirigeants et directeurs de pôle d'agences marketing, communication et SEO françaises.

### Entrées Fournies par l'Agence
- Un fichier de configuration par client final :
  - Nom d'affichage de la marque cliente.
  - Liste de 5 concurrents directs identifiés.
  - URLs publiques à surveiller pour chaque concurrent : grilles tarifaires (`/pricing`), notes de version (`/changelog`), articles de blog récents, pages recrutement/offres d'emploi, communiqués de presse.

### Livrable
- **Un rapport PDF hebdomadaire de 3 à 6 pages**, 100 % marque blanche (zéro mention de l'outil ou du prestataire) :
  - **Synthèse exécutive** de la semaine.
  - **5 à 10 signaux qualifiés** classés par niveau d'impact (Élevé, Moyen, Faible).
  - Chaque signal comporte :
    - Source exacte (URL publique) et date de capture.
    - Description objective : « Ce qui a changé » (comparaison différentielle N vs N-1).
    - Analyse : « Interprétation stratégique » (séparation nette fait / opinion).
    - Recommandations : 3 actions concrètes et activables par l'agence ou son client.
  - Si aucune modification notable n'est constatée sur un concurrent, le rapport l'indique explicitement sans inventer de faux signal.
- **Historique consultable** : Conservation des instantanés pour comparaison dans le temps.

### Engagements Opérationnels
- Temps de traitement humain : Moins de 45 minutes par rapport client.
- Zéro accès à des pages authentifiées ou protégées par login/mot de passe.

---

## 2. Offre : Vibe-Audit (Audit Express de Sécurité pour Apps IA)

### Contexte & Problème
Des créateurs d'entreprise et fondateurs non techniques publient des applications web fonctionnelles conçues en quelques jours via des plateformes d'IA générative (Lovable, Bolt, Cursor). Beaucoup ignorent les risques critiques liés aux clés d'API exposées, aux bases sans politique de sécurité ou aux autorisations mal configurées.

### Cible
- Fondateurs non techniques francophones ayant déployé ou s'apprêtant à déployer une application générée par IA.

### Prérequis Absolu & Entrées
- **Consentement écrit préalable** : Fichier `consent/<client>.md` signé et enregistré avant toute analyse (mentionnant signataire, périmètre d'URL/dépôt, dates d'autorisation).
- Accès en lecture seule au dépôt de code (ou archive ZIP).
- URL publique de production ou de pré-production.
- Export du schéma de base de données et des politiques de sécurité (ex. politiques RLS Supabase) fourni par le client.

### Périmètre des Contrôles Passifs & Locaux
1. **Secrets exposés** : Recherche de clés privées, tokens d'API, identifiants dans le code source et dans l'historique git.
2. **Politiques de sécurité des données (RLS)** : Détection des tables publiques dépourvues de Row Level Security ou dotées de règles permissives `true`.
3. **Autorisation client vs serveur** : Vérification que les opérations sensibles ne reposent pas sur une validation exclusive dans le navigateur.
4. **Exposition frontend** : Présence de clés de service (`service_role`) ou secrets dans les variables d'environnement embarquées dans le bundle JS.
5. **Dépendances vulnérables** : Analyse statique des paquets déclarés (`npm audit`, `pip-audit`).
6. **Configuration réseau & HTTP** : Analyse passive des en-têtes HTTP de sécurité (CSP, HSTS, CORS) et configuration TLS sur l'URL publique consentie.
7. **Paiement (si applicable)** : Vérification de la validation côté serveur des signatures de webhooks (Stripe/LemonSqueezy) contre les fraudes de contournement.

### Livrable
- **Rapport PDF synthétique et pédagogique (livré sous 48h)** :
  - Tableau de synthèse avec classification par niveau de risque : Critique, Élevé, Moyen, Faible.
  - Pour chaque constat vérifié : preuve reproductible, impact concret pour le business, correctif pas à pas.
  - **Prompt prêt à coller** dans Lovable, Bolt ou Cursor pour appliquer la correction immédiatement.
  - Section transparente listant explicitement ce qui n'a **pas** été testé.
- **Re-contrôle à J+14** : Vérification gratuite sur demande pour confirmer que les correctifs appliqués ont bien comblé les failles.
