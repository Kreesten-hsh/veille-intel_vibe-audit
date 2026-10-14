# Spécification Produit & Design : Vibe-Audit

## 1. Vision & Philosophie du Livrable
Vibe-Audit est un audit de cybersécurité express (48h), à prix fixe et non destructif, taillé sur mesure pour les fondateurs d'applications construites avec Lovable, Bolt.new, Cursor et le no-code.
Le livrable rompt radicalement avec les rapports de pentest traditionnels (scanners automatisés de 60 pages en PDF portrait illisibles) :
- **Format 100% Paysage (16:9 / A4 Paysage)** : Conçu pour être lu nativement sur écran d'ordinateur (MacBook / PC portable) sans défilement vertical fastidieux.
- **Longueur calibrée : 5 pages maximum** : Chaque page remplit un rôle unique, synthétique et immédiatement actionnable.
- **Double niveau de lecture** : Une colonne "Impact Métier & Preuve" pour le fondateur non technique, et une colonne "Prompt Prêt à Copier-Coller" pour l'IA (Lovable / Bolt / Cursor).
- **Zéro Emoji, Iconographie Vectorielle Pro** : Utilisation exclusive d'icônes SVG fines de la bibliothèque open-source **Lucide Icons**.

---

## 2. Décomposition Page par Page (Format Paysage 16:9)

### PAGE 1 : Tableau de Bord Exécutif & Score de Posture
- **En-tête** : Logo Vibe-Audit, nom de l'application cible, date de capture, version / commit analysé, auditeur certifié (Kreesten Agboton).
- **Jauge Circulaire Centrale (Donut Severity)** : Score de santé global (ex: *64 / 100 - Risque Modéré*) avec anneau à dégradé Cyan (`#00F0FF`) vers Violet (`#8B5CF6`).
- **Cartes Métriques Supérieures (Stats Cards)** :
  - Nombre de failles Critiques 🔴, Élevées 🟠, Moyennes 🟡, Faibles 🟢.
- **Synthèse Exécutive en 3 phrases** : Ce que le fondateur et ses investisseurs doivent comprendre en 30 secondes.
- **Matrice du Périmètre** : Ce qui a été testé (endpoints publics, configuration Supabase, bundles JS) vs Ce qui est hors périmètre (infrastructures Stripe, serveurs tiers).

### PAGE 2 : Failles Critiques — Base de Données & Données Utilisateurs (Supabase RLS & IDOR)
- **Disposition en 2 Split-Cards horizontales** :
  - **Constat SEC-01** : Absence ou mauvaise configuration de Row Level Security (RLS) sur Supabase (tables `users` ou `orders` publiquement lisibles).
  - **Constat SEC-02** : IDOR (Insecure Direct Object Reference) permettant d'accéder aux profils et documents d'autres utilisateurs.
- **Structure de chaque Split-Card** :
  - *Volet Gauche (Compréhension Métier)* : Badge sévérité 🔴 Critique, impact business vulgarisé, preuve reproductible (commande `curl` passive).
  - *Volet Droit (Action Immédiate)* : Bloc terminal sombre avec le **Prompt exact prêt à coller** dans Lovable / Bolt / Cursor (avec la commande SQL RLS exacte).

### PAGE 3 : Failles Élevées — Authentification, Clés API & Paiements
- **Disposition en 2 Split-Cards horizontales** :
  - **Constat SEC-03** : Clés API secrètes exposées dans le bundle front-end JavaScript (`VITE_` ou `NEXT_PUBLIC_` mal scopés).
  - **Constat SEC-04** : Webhook Stripe non signé ou vérification côté client vulnérable aux faux paiements.
- **Pour chaque point** : Preuve réseau horodatée + Prompt de refactorisation vers une Edge Function / route backend sécurisée.

### PAGE 4 : Hygiène d'Infrastructure, Headers HTTP & CORS
- **Tableau de Diagnostic de Surface (Dark Data Table)** :
  - Headers HTTP vérifiés : Content-Security-Policy (CSP), Strict-Transport-Security (HSTS), X-Frame-Options (Clickjacking), X-Content-Type-Options.
  - Statut par point : `Sécurisé` (point vert) ou `Manquant / Vulnérable` (point rouge/orange).
- **Constat SEC-05** : Politique CORS permissive (`Access-Control-Allow-Origin: *`) avec credentials.
- **Prompt Universel de Durcissement** : Configuration des headers pour Next.js, Vite ou Cloudflare Workers.

### PAGE 5 : Plan de Remédiation Pas-à-Pas & Engagement Re-Check à J+14
- **Roadmap Chronologique de Remédiation** :
  - *Étape 1 (15 minutes)* : Application des 2 prompts RLS critiques dans Supabase.
  - *Étape 2 (20 minutes)* : Déplacement des clés API privées et signature des webhooks Stripe.
  - *Étape 3 (10 minutes)* : Ajout des headers de sécurité.
- **Badge & Protocole de Re-Contrôle J+14** :
  - Procédure pour demander la ré-évaluation gratuite après correction.
  - Modèle de badge numérique : *"Audité et Re-contrôlé par Vibe-Audit - Sécurité Validée"*.
- **Décharge Légale & Confidentialité** : Rappel de l'accord bilatéral NDA et destruction des traces d'audit.

---

## 3. Charte Graphique & Système de Design

### Palette de Couleurs (Dark Cyber Theme)
- **Fond d'Écran Principal (Background)** : `#0A0F20` (Bleu nuit spatial profond).
- **Surfaces des Cartes (Cards & Panels)** : `#11182D` avec bordure fine `1px solid rgba(255, 255, 255, 0.08)`.
- **Blocs Terminaux / Prompts (Code Surface)** : `#060A14` avec bordure d'accentuation cyan subtile.
- **Palette de Statuts & Sévérités** :
  - 🔴 **Critique** : `#EF4444` (Lueur rouge `rgba(239, 68, 68, 0.15)`)
  - 🟠 **Élevé** : `#F97316` (Ambre soutenu)
  - 🟡 **Moyen** : `#F59E0B` (Jaune cyber)
  - 🟢 **Sécurisé / Faible** : `#10B981` (Vert émeraude néon)
- **Accents Technologiques & Graphiques** :
  - **Cyan Néon** : `#00F0FF` (Chiffres clés, barres de progression, bordures actives)
  - **Violet Électrique** : `#8B5CF6` (Dégradé secondaire du donut chart)
- **Texte & Lisibilité (Conformité WCAG AAA)** :
  - Titres & Chiffres : `#FFFFFF` (Blanc pur)
  - Corps de texte : `#94A3B8` (Slate gris bleuté, contraste 9:1 sur `#0A0F20`)
  - Code & Variables : `#E2E8F0`

### Typographie (Google Fonts - Open Source)
1. **Titres & Métriques (Display)** : **Space Grotesk** ou **Plus Jakarta Sans** (géométrique, high-tech, moderne).
2. **Corps de Texte & Tableaux (Body)** : **Inter** (lisibilité sans égale à toutes les résolutions).
3. **Prompts IA & Code Snippets (Monospace)** : **JetBrains Mono** (ligatures de programmation, lisibilité immédiate).

### Iconographie (Lucide Icons SVG)
- **Aucun emoji dans les livrables.**
- Icônes SVG vectorielles au trait fin (stroke-width: 1.75px) :
  - `ShieldCheck` / `ShieldAlert` : Statut de sécurité global.
  - `Database` : Supabase / RLS.
  - `KeyRound` : Fuites de clés API.
  - `CreditCard` : Paiements & Stripe Webhooks.
  - `Terminal` : Blocs de prompts de remédiation.
  - `CheckCircle2` / `XCircle` : Validations et échecs de tests.

---

## 4. Composants Graphiques Signature

1. **Donut de Gravité SVG** : Anneau à double dégradé (Cyan vers Violet) affichant le score de santé en son centre avec légende de répartition des alertes.
2. **Pill Badges avec LED Pulsée** : Badges de sévérité compacts dotés d'une puce lumineuse colorée.
3. **Split-Card Constat & Prompt** :
   - Côté gauche : Titre, impact en français clair, preuve sous forme d'appel API.
   - Côté droit : En-tête de terminal *"PROMPT PRÊT À COLLER"* avec bouton de copie et prompt formulé sans ambiguïté pour l'outil IA.
