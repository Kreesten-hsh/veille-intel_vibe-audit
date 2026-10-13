# Spécification Fonctionnelle & Technique : Vibe-Audit

## 1. Vision du Produit
Vibe-Audit est un audit de cybersécurité express (48h), à prix fixe et non destructif, taillé sur mesure pour les applications créées avec des outils de développement assistés par IA (Lovable, Bolt.new, Cursor, v0, Bubble).
Le livrable transforme des vulnérabilités complexes en **prompts de remédiation directement exploitables par l'IA**, sans obliger le fondateur à apprendre la cybersécurité.

## 2. Périmètre d'Audit & Failles Analysées

L'audit couvre 5 catégories de risques critiques récurrents dans les applications "vibe-coded" :

### A. Fuite de Clés Secrètes & Variables d'Environnement
- **Risque** : Clés API privées exposées dans le bundle JavaScript front-end (ex. clés secrètes Stripe `sk_live_...`, clés Supabase `service_role`, clés OpenAI / Anthropic / Resend).
- **Méthode** : Inspection des sources JS bundlées (`_app.js`, `main.js`), des requêtes réseau au chargement, et détection de préfixes interdits dans les variables publiques (`NEXT_PUBLIC_`, `VITE_`).
- **Livrable** : Preuve exacte de la clé exposée + Prompt pour déplacer l'appel vers une Edge Function / API backend sécurisée.

### B. Contrôle d'Accès aux Données (Supabase RLS / Firebase Rules)
- **Risque** : Row Level Security (RLS) désactivé ou mal configuré sur les tables sensibles (`users`, `payments`, `profiles`, `orders`). N'importe quel internaute peut requêter directement l'API REST de Supabase avec la clé anon et aspirer la base de données.
- **Méthode** : Requête passive ciblée sur l'API Supabase cliente avec la clé publique fournie dans le front-end pour vérifier la ségrégation des données entre utilisateurs (IDOR).
- **Livrable** : Preuve reproductible (`curl`) + Règle SQL RLS exacte prête à être collée dans Supabase ou promptée dans Cursor.

### C. Authentification & Session
- **Risque** : Endpoints non protégés, vérification de rôle utilisateur côté client uniquement (`isAdmin: true` dans le localStorage sans vérification serveur).
- **Méthode** : Test de contournement d'accès aux routes d'administration ou aux fonctions de modification.
- **Livrable** : Preuve de contournement + Prompt pour implémenter un middleware de validation de session sécurisé.

### D. Webhooks de Paiement (Stripe / Lemonsqueezy)
- **Risque** : Endpoint de réception du webhook sans validation de la signature cryptographique (`stripe-signature`), permettant à un attaquant de forger de faux événements de paiement et d'obtenir des accès gratuits.
- **Méthode** : Revue de la logique de vérification du webhook.
- **Livrable** : Prompt de configuration de la validation de signature `stripe.webhooks.constructEvent()`.

### E. Headers de Sécurité & CORS
- **Risque** : Autorisation de tous les domaines (`Access-Control-Allow-Origin: *`) combinée avec des cookies de session, absence de CSP (Content Security Policy).
- **Méthode** : Analyse passive des headers HTTP de réponse.
- **Livrable** : Configuration prête à l'emploi des headers de sécurité (Next.js / Vite / Cloudflare).

---

## 3. Design & Structure du Rapport Livrable (4 à 6 Pages PDF)

### Charte Visuelle du Rapport
- **Format** : Document PDF A4 portrait élégant, orienté "Directeur de Produit".
- **Typographie** : Space Grotesk (Titres majeurs), Inter (Corps de texte), JetBrains Mono (Prompts & Extraits de code).
- **Palette** :
  - Fond : Blanc pur (`#FFFFFF`) avec encadrés gris slate légers (`#F8FAFC`).
  - Titres et structure : Deep Dark Navy (`#090D16`).
  - Niveaux de sévérité :
    - 🔴 **Critique** (`#EF4444`) : Accès aux données de tous les utilisateurs ou vol d'argent possible.
    - 🟠 **Élevé** (`#F97316`) : Contournement d'authentification ou fuite de PII.
    - 🟡 **Moyen** (`#F59E0B`) : Headers manquants, mauvaise pratique de cache.
    - 🟢 **Faible / Info** (`#10B981`) : Optimisation d'hygiène de code.

### Structure Type d'une Fiche de Constat (1 page par faille majeure)
1. **En-tête** : Identifiant de la faille (`SEC-01`), Sévérité, Composant touché (ex. *Supabase Table: users*).
2. **Impact Business Vulgarisé** : Expliqué en 2 phrases simples, sans jargon inutile.
3. **Preuve Reproductible** : Description factuelle de la méthode de reproduction (en lecture seule).
4. **Le Prompt Correctif Vibe-Coding** :
   ```markdown
   > PROMPT PRÊT À COLLER DANS LOVABLE / BOLT / CURSOR :
   "Modifie la politique Row Level Security de la table 'invoices' dans Supabase pour que seuls les utilisateurs authentifiés dont l'auth.uid() correspond à user_id puissent lire et modifier leurs propres factures. Voici la règle SQL à appliquer : [...]"
   ```
5. **Re-Test Checklist** : L'action précise pour vérifier que le correctif fonctionne.

---

## 4. Cadre Légal & Formulaire de Consentement Obligatoire

Conformément au Guardrail 3 du projet, **aucune application n'est inspectée sans consentement écrit préalable enregistré**.

### Le Formulaire d'Autorisation (Signé en 2 minutes en ligne) :
- Identification du propriétaire légitime de l'application.
- Déclaration expresse autorisant Kreesten Agboton (Vibe-Audit) à inspecter les endpoints convenus.
- Engagement de non-destruction et de non-perturbation du service par Vibe-Audit.
- Clause de confidentialité intégrale (NDA bilatéral) garantissant le secret absolu sur les failles découvertes et le code source.
