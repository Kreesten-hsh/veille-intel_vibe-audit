# Spécification de Structure : Rapports Vibe-Audit

Ce document définit l'architecture modulaire, les champs obligatoires, les critères d'acceptation de contenu et les règles d'adaptation dynamique du rapport d'audit Vibe-Audit (3 à 6 pages A4 paysage).

---

## 1. Principes Structurels

1. **Format Unifié Sombre (`#0A0F20`) sur Toutes les Pages**  
   L'ensemble du document (Page 1 jusqu'à Page 6) est habillé du même arrière-plan bleu nuit spatial (`#0A0F20`), offrant une cohérence visuelle parfaite sans rupture de style.
2. **Volume Réel Adaptable (3 à 6 pages)**  
   Le rapport s'adapte strictement au nombre de constats réels sans remplissage artificiel.
3. **Distribution Fluide par Importance Réelle**  
   - Les constats sont ordonnés par gravité décroissante : Critique, Élevé, Moyen, Faible.
   - Si une application ne comporte **aucune faille critique**, les constats débutent immédiatement par les failles Élevées.
4. **Vérité Statistique & Séparation des Métriques**  
   - La barre empilée ne représente que les failles de sécurité réelles. Les contrôles jugés conformes font l'objet d'un comptage séparé.
   - Aucun composant non testé (ex: Stripe) ne peut être qualifié de "sain" ou "sécurisé".

---

## 2. Grille de Contrôle Qualité & Critères d'Acceptation de Contenu

Tout rapport généré par Vibe-Audit doit obligatoirement valider les 8 contrôles suivants :

| Contrôle | Critère d'acceptation obligatoire |
|---|---|
| **1. Cohérence des chiffres** | Le total de la barre de gravité correspond exactement à la somme arithmétique des constats (`Critique + Élevé + Moyen + Faible`). Les contrôles sans anomalie sont présentés dans une carte indépendante distincte. |
| **2. Cohérence du périmètre** | Tout composant déclaré hors périmètre dans la matrice de couverture ne peut faire l'objet d'aucune appréciation de sécurité dans le résumé exécutif (mention obligatoire : *« Non évalué dans cette mission »*). |
| **3. Traçabilité des preuves** | Chaque constat technique précise le contexte exact de capture : horodatage UTC, méthode HTTP, type de clé utilisé (ex: clé `anon` publique) et preuve formelle de dénombrement (ex: en-tête de réponse `Content-Range: 0-1/142`). |
| **4. Neutralité des statuts** | Les critères de validation d'une correction proposée utilisent des indicateurs visuels neutres (cases non cochées). Le vert est strictement réservé aux contrôles déjà testés et validés. Le re-check J+14 est indiqué comme éligible ou inclus sur demande, jamais comme déjà réalisé. |
| **5. Remédiation nuancée** | Tout prompt SQL ou script de correction explicite ses hypothèses d'architecture (présence de la colonne `user_id`, isolation multi-tenant, opérations couvertes `SELECT`, `INSERT`, `UPDATE`, `DELETE`). |
| **6. Mention de démonstration** | Tout rapport d'échantillon commercial ou démonstrateur comporte un encadré visible stipulant que les données et l'application cible sont fictives et issues d'un environnement contrôlé (sandbox). |
| **7. Références méthodologiques exactes** | Les références citées (OWASP, NIST) correspondent exactement au type de test effectué (ex: `OWASP WSTG-ATHZ-02` et `OWASP API1:2023 (BOLA)` pour les contrôles d'accès Supabase, et non des références d'interfaces d'administration). |
| **8. Export PDF haute fidélité** | Le PDF fait exactement le nombre de pages prévu, le texte reste sélectionnable, aucun élément ne déborde du format A4 paysage (297 × 210 mm) et les contrastes respectent WCAG AA. |

---

## 3. Décomposition des Pages (Fond Sombre `#0A0F20`)

### Page 1 : Synthèse Exécutive Décideur
- **Bandeau de démonstration** (si échantillon commercial).
- **En-tête & Métadonnées** : Cible, date de l'audit, auditeur (Kreesten Agboton), référence de consentement écrit.
- **Barre de gravité empilée** : Ventilation exacte des vulnérabilités uniquement (ex: 2 Élevés, 1 Moyen, 1 Faible).
- **Indicateur de contrôles conformes** : Bloc séparé « Contrôles examinés sans anomalie : 4 ».
- **Synthèse en 3 phrases** : Constat global, impact concret et faisabilité de la remédiation.
- **3 Actions Prioritaires Immédiates** : Liste numérotée des correctifs urgents.
- **Matrice de couverture de surface** : Liste des composants testés vs composants hors périmètre.

### Pages 2 à 4 : Fiches Détaillées des Constats (Format Split-Card)
- **En-tête de constat** : Badge de sévérité + Badge `Constat confirmé` + Identifiant (ex: `SEC-01`) + Composant.
- **Colonne Gauche (Métier & Preuve)** :
  - Encadré d'impact métier en français clair pour le fondateur.
  - Boîte terminal sombre avec horodatage UTC, commande `curl -i` exacte, en-tête HTTP prouvant le résultat (`Content-Range`), et données sensibles masquées (`***`).
- **Colonne Droite (Remédiation & Validation)** :
  - Badge `Correction proposée` + Outil cible (`Lovable / Bolt / Cursor / Supabase`).
  - Bloc prompt IA avec hypothèses d'architecture clairement documentées.
  - Checklist de validation post-correction avec icônes neutres (cases non cochées).

### Pages 5 et 6 : Kit de Remédiation, Feuille de Route & Périmètre (si applicable)
- **Roadmap chronologique** : Étape 1 (immédiat), Étape 2 (sous 48h), Étape 3 (moyen terme).
- **Modalités de Re-Check J+14** : Procédure de re-test gratuit sur demande après déploiement des correctifs.
- **Périmètre, Limites et Confidentialité** : Rappel de la méthode non destructive, exclusion ferme de toute intrusion active ou test de déni de service, et engagement formel de destruction des données.
