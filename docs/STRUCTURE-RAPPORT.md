# Spécification de Structure : Rapports Vibe-Audit

Ce document définit l'architecture modulaire, les champs obligatoires et les règles d'adaptation dynamique du rapport d'audit de sécurité Vibe-Audit (3 à 6 pages A4 paysage).

---

## 1. Principes Structurels

1. **Volume Variable Réel (3 à 6 pages)**  
   Le rapport s'adapte strictement au nombre et à la complexité des constats réels. On ne remplit jamais de pages blanches artificielles pour faire du volume.
2. **Distribution Fluide par Importance Réelle (Non figée par gravité)**  
   - Les constats sont triés par ordre de priorité opérationnelle décroissante : Critique, puis Élevé, Moyen, Faible.
   - Si une application ne comporte **aucune faille critique**, la section principale traite immédiatement les constats Élevés. On n'invente jamais de catégorie vide ni de risque artificiel pour remplir un modèle.
3. **Double Niveau de Lecture Systématique**  
   Chaque page technique permet à un fondateur non technique de comprendre le risque métier en 30 secondes, et fournit à son développeur ou son agent IA (Lovable, Bolt, Cursor) les éléments exacts pour corriger et valider le correctif.
4. **Trois Statuts Distincts et Infalsifiables**  
   - `Constat confirmé` : Faille testée, reproduite et documentée avec preuve.
   - `Correction proposée` : Prompt IA et marche à suivre suggérés pour corriger.
   - `Correction vérifiée` : Re-contrôle effectif post-déploiement (uniquement mentionné si la prestation de re-check à J+14 a été réellement commandée et exécutée).

---

## 2. Décomposition Modulaire des Pages

### Page 1 : Vue d'Ensemble Exécutive (Fond Sombre `#0A0F20`)
- **Objectif** : Permettre au fondateur, à ses associés ou investisseurs de saisir l'état de sécurité et les priorités absolues en une minute.
- **Champs obligatoires** :
  - **Métadonnées de l'audit** : Nom de l'application, URL cible, date de capture, version ou commit inspecté, auditeur (Kreesten Agboton).
  - **Statut légal de consentement** : Référence de l'accord écrit signé préalable.
  - **Barre de gravité empilée (Stacked Bar)** : Nombre exact de constats par sévérité (ex: 0 Critique, 2 Élevés, 1 Moyen, 1 Faible). Aucun pourcentage arbitraire.
  - **Synthèse exécutive (3 phrases clés)** : Constat global vulgarisé, exposition financière/données, et recommandation de tête.
  - **Bloc "3 Actions Prioritaires Immédiates"** : Les 3 correctifs à déployer en priorité.
  - **Matrice de couverture sommaire** : Domaines testés vs hors périmètre.

---

### Page 2 : Profil d'Application & Matrice de Couverture (Fond Clair `#F4F7FB`)
- **Objectif** : Poser la cartographie technique observée et définir avec précision les frontières du test.
- **Champs obligatoires** :
  - **Composants observés** : Frontend (Vite/Next.js/React), Backend & API (Supabase Edge Functions, routes serveur), Base de données (PostgreSQL Supabase), Services tiers (Stripe, Resend, etc.).
  - **Schéma d'architecture simplifié** : Cartographie des flux utilisateurs, requêtes API et accès base.
  - **Matrice de couverture détaillée** :
    - *Domaine* (RLS Supabase, Authentification, Bundles JS / Clés API, Webhooks Paiement, Headers & CORS).
    - *Statut d'inspection* : `Examiné avec constat`, `Examiné conforme`, ou `Non testé (hors périmètre)`.
    - *Outils & techniques passives employés*.

---

### Pages 3 et 4 : Fiches Détaillées des Constats (Fond Clair `#F4F7FB`)
- **Capacité** : 1 à 2 constats majeurs par page paysage en format split-card.
- **Règle d'enchaînement** : Les fiches s'enchaînent par ordre de sévérité réelle sans saut de page vide.
- **Champs obligatoires de chaque fiche (`FindingSplitCard`)** :
  1. **En-tête** :
     - Identifiant unique (ex: `SEC-01`, `SEC-02`).
     - Titre explicite du constat.
     - Badge de gravité (Critique, Élevé, Moyen ou Faible).
     - Badge de statut : `Constat confirmé`.
  2. **Colonne Gauche — Compréhension & Preuve** :
     - *Composant affecté* (ex: Table Supabase `orders`, Clé secrète dans `.env.production`).
     - *Impact métier* : Conséquence concrète pour l'entreprise (ex: "N'importe quel visiteur peut lire les factures et emails des 140 clients sans s'authentifier").
     - *Preuve reproductible* : Commande `curl` passive non destructive et réponse HTTP avec données masquées (`***`).
  3. **Colonne Droite — Remédiation & Validation** :
     - *Statut du correctif* : `Correction proposée`.
     - *Outil cible* : Lovable, Bolt.new, Cursor ou commande SQL manuelle.
     - *Bloc Prompt IA* : Prompt exhaustif sans ambiguïté prêt à coller dans l'assistant.
     - *Critères de validation* : Checklist de 2 à 3 points concrets pour tester que la vulnérabilité est effectivement comblée.

---

### Page 5 : Kit de Remédiation IA & Dépendances de Correction (Si applicable)
- **Objectif** : Regrouper les prompts transversaux ou complexes nécessitant un ordre de déploiement strict.
- **Champs obligatoires** :
  - Tableau des dépendances (ex: "Appliquer la politique RLS avant de modifier les clés API").
  - Prompts d'ajustement des headers de sécurité (CSP, HSTS, CORS) et configuration d'hébergement (Vercel, Netlify, Cloudflare).
  - Critères de non-régression applicative.

---

### Page 6 : Feuille de Route, Périmètre, Limites et Confidentialité (Fond Clair `#F4F7FB`)
- **Objectif** : Clôturer le livrable sur un calendrier d'action réaliste et cadrer formellement les responsabilités et limites de l'audit.
- **Champs obligatoires** :
  - **Feuille de route chronologique** : Étape 1 (immédiat, < 1h), Étape 2 (sous 48h), Étape 3 (durcissement à moyen terme).
  - **Protocole de Re-Check à J+14** :
    - Mention explicite : *Inclus* (si formule standard/complète) ou *Optionnel sur demande*.
    - Modalités de vérification après mise en ligne des correctifs.
  - **Section "Périmètre, Limites et Confidentialité"** :
    - Nature de l'évaluation : Audit passif et vérifications d'architecture, non destructif.
    - Exclusions fermes : Aucune tentative de déni de service (DDoS), aucune intrusion sur serveurs tiers hébergeurs, aucune ingénierie sociale.
    - Engagement de confidentialité : Engagement formel de non-divulgation et destruction des traces et clés transmises après livraison.

---

## 3. Matrice d'Adaptation Dynamique selon le Nombre de Constats

| Nombre de Constats Majeurs | Nombre Total de Pages | Répartition des Pages |
|---|---|---|
| **1 à 2 constats** | **3 pages** | P1 (Vue d'ensemble) → P2 (Constats 1 & 2 avec prompts) → P3 (Périmètre, limites, roadmap) |
| **3 à 4 constats** | **4 pages** | P1 (Vue d'ensemble) → P2 (Profil & Couverture) → P3 (Constats 1 à 4) → P4 (Roadmap, limites & confidentialité) |
| **5 à 6 constats** | **5 ou 6 pages** | P1 (Vue d'ensemble) → P2 (Profil & Couverture) → P3 (Constats 1 & 2) → P4 (Constats 3 & 4) → P5 (Constats 5 & 6 + Prompts) → P6 (Roadmap & Limites) |

---

## 4. Règles Rédactionnelles Obligatoires

1. **Aucune promesse absolue de sécurité** : L'absence de faille détectée sur un composant signifie qu'aucune anomalie n'a été mise en évidence lors des tests passifs, jamais qu'un système est "100% inviolable".
2. **Neutralité factuelle** : Formulations directes et précises, absence de superlatifs alarmistes ("faille catastrophique", "sécurité désastreuse") comme d'autosatisfaction.
3. **Respect du secret** : Tous les tokens réels, identifiants de sessions et données personnelles visibles lors des captures de preuves doivent être masqués (`Bearer sk_live_***`).
