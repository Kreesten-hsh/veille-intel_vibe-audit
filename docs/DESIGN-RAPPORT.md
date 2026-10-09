# Système de Design : Rapports Vibe-Audit

Ce document établit la charte formelle, les jetons de conception (tokens) et les spécifications de composants pour la génération des rapports d'audit de sécurité Vibe-Audit.

L'objectif esthétique est résolument sobre, éditorial et statutaire : un rapport d'audit formel imprimable, exempt d'artéfacts génériques associés aux interfaces générées par IA (pas de dégradés criards, pas de coins très arrondis, pas de bandeaux latéraux saturés, pas de titres en majuscules, pas d'émoticônes ni de tirets cadratins).

---

## 1. Principes Directeurs

1. **Hiérarchie typographique éditoriale** : Titres en police avec empattement (serif système), corps de texte lisible en sans-serif système, preuves techniques en chasse fixe (monospace système).
2. **Support papier et encre** : Fond papier blanc cassé très léger, encre textuelle quasi noire, bordures fines en gris neutre.
3. **Information portée par le texte** : Chaque niveau de gravité est écrit intégralement en toutes lettres (Critique, Élevé, Moyen, Faible). La couleur n'est qu'un renfort secondaire sobre et ne porte jamais seule l'information.
4. **Accessibilité rigoureuse (WCAG AA)** : Contraste minimal de 4,5:1 pour le texte courant et les métadonnées sur leur arrière-plan respectif.
5. **Économie de surface (densité utile)** : Mise en page conçue pour le format A4 (3 à 4 pages denses), éliminant les blancs disproportionnés et évitant la fragmentation des preuves et des correctifs.

---

## 2. Jetons de Conception (Design Tokens)

### 2.1. Couleurs (Palette Chromatique)

| Jeton (Token) | Valeur Hex | Rôle | Ratio de Contraste |
|---|---|---|---|
| `--color-paper` | `#faf9f5` | Fond de page principal (blanc cassé chaud) | Base de réflectance |
| `--color-card-bg` | `#ffffff` | Fond des blocs de contenu et tableaux | Base blanche neutre |
| `--color-ink-primary` | `#1c1917` | Texte principal, titres, en-têtes (encre dense) | 14,2:1 sur papier |
| `--color-ink-muted` | `#57534e` | Métadonnées, libellés secondaires, dates | 5,8:1 sur papier |
| `--color-border-subtle`| `#e7e5e4` | Filets de séparation de sections, bordures | Décoratif structuré |
| `--color-border-strong`| `#a8a29e` | Filets d'accentuation, séparateurs majeurs | 3,2:1 |
| `--color-accent` | `#1e3a5f` | Accent institutionnel unique (bleu nuit sourd) | 9,8:1 sur papier |
| `--color-proof-bg` | `#1e232a` | Fond des blocs de preuve technique (ardoise sombre) | Base sombre |
| `--color-proof-text` | `#e2e8f0` | Texte des extraits de sortie technique | 11,5:1 sur fond sombre |
| `--color-proof-cmd` | `#7dd3fc` | Commandes exécutées dans la preuve | 8,9:1 sur fond sombre |

### 2.2. Niveaux de Gravité (Teintes Sourdes)

Chaque gravité associe une bordure sobre, un fond atténué et un texte textuel conforme au contraste 4,5:1 minimum :

| Gravité | Texte / Bordure | Fond | Contraste Texte/Fond | Usage |
|---|---|---|---|---|
| **Critique** | `#7f1d1d` (Rouge brique sombre) | `#fef2f2` | 7,1:1 | Risque immédiat de compromission totale ou de fuite de données |
| **Élevé** | `#9a3412` (Ocre brûlé) | `#fff7ed` | 5,6:1 | Vulnérabilité exploitable contournant un contrôle métier |
| **Moyen** | `#854d0e` (Brun terreux) | `#fefce8` | 5,9:1 | Configuration trop permissive ou bibliothèque vulnérable |
| **Faible** | `#1e40af` (Bleu ardoise) | `#eff6ff` | 7,8:1 | Absence de durcissement défensif ou en-tête manquant |

### 2.3. Typographie

| Rôle | Famille | Graisse | Taille | Interligne |
|---|---|---|---|---|
| Titre de document (H1) | Georgia, "Times New Roman", serif | 700 (Bold) | 22pt / 26px | 1.25 |
| Titre de section (H2) | Georgia, "Times New Roman", serif | 700 (Bold) | 14pt / 18px | 1.30 |
| Titre de constat (H3) | Georgia, "Times New Roman", serif | 600 (Semibold) | 11.5pt / 15px | 1.30 |
| Corps de texte | -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif | 400 (Regular) | 9.5pt / 12.5px | 1.45 |
| Métadonnées & Libellés | -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif | 600 (Semibold) | 8.5pt / 11px | 1.35 |
| Preuves & Code | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace | 400 (Regular) | 8pt / 10.5px | 1.35 |

### 2.4. Espacements et Filets

- **Échelle d'espacement** : `space-1` (4px), `space-2` (8px), `space-3` (12px), `space-4` (16px), `space-5` (20px), `space-6` (24px).
- **Filets (Borders)** : 1px plein (`solid`), coins droits ou adoucis au strict minimum (rayon maximal de 2px à 3px sur les conteneurs). Aucun effet "pilule" ni pastille ronde.

---

## 3. Spécifications des Composants

### 3.1. EnTête de Rapport (`Header`)
- **Structure** : Titre formel du document, métadonnées structurées sur deux colonnes (Application auditée, Date, Auditeur, Statut).
- **Auteur** : Formule sobre indiquant l'auditeur indépendant (ex. « Kreesten, consultant indépendant »).
- **Statut** : Libellé discret « Échantillon commercial » inséré dans la ligne de métadonnées, sans mention parasite.
- **Do** : Titre en serif sobre, date explicite, mention claire de la propriété de l'application.
- **Don't** : Bannir les logos décoratifs, les badges flottants, les chemins absolus locaux et le mot cabinet.

### 3.2. Bilan des risques (`GravitySummaryBar`)
- **Structure** : Alignement horizontal de 4 compteurs compacts (Critique, Élevé, Moyen, Faible) avec étiquette textuelle en petites capitales et chiffre saillant.
- **Accessibilité** : La couleur d'accentuation borde le bloc d'un fin filet de 2px supérieur sans envahir l'arrière-plan.
- **Do** : Permettre au lecteur d'appréhender le volume global de risques en un coup d'œil.
- **Don't** : Pas de pastilles circulaires fluorescentes ni de barres de progression graphiques trompeuses.

### 3.3. Tableau de synthèse (`SummaryTable`)
- **Structure** : Tableau rigoureux à lignes délimitées par des filets gris fins (`#e7e5e4`). Colonnes : Identifiant, Intitulé du constat, Gravité, Composant cible, Méthode de vérification.
- **Ordre** : Tri décroissant strict selon la sévérité (Critique d'abord, puis Élevé, Moyen, Faible).

### 3.4. Constats détaillés (`FindingCard`)
- **Structure** (pleine largeur, une seule colonne) :
  1. *Ligne d'en-tête* : Identifiant (ex. SEC-01), intitulé clair et mention textuelle de gravité.
  2. *Impact métier* : Une phrase synthétique exposant la conséquence directe pour le fondateur.
  3. *Plan de correction* : Liste numérotée étape par étape.
  4. *Preuve reproductible* : Conteneur monospace pleine largeur sombre (`BlocPreuve`), commandes exactes et sorties réelles sans coupure de mots (`white-space: pre`).
  5. *Prompt de correction* : Bloc distinct (`BlocPromptCorrection`), clairement séparé, avec bordure fine pointillée discrète.

### 3.5. Bloc de preuve (`ProofBox`)
- **Règles** : Fond ardoise sombre mat (`#1e232a`), texte clair lisible, pleine largeur sous le correctif, `white-space: pre` sans césure automatique, masquage des secrets réels (`***`).
- **Do** : Afficher les commandes exactes exécutées et leurs sorties réelles vérifiées.
- **Don't** : Pas de texte tronqué sans indication, pas de texte synthétique inséré dans une sortie de commande.

### 3.6. Bloc de prompt de correction (`PromptBox`)
- **Intitulé standard** : « Prompt de correction » (mention unique en tête de section : « Les prompts ci-dessous sont prêts à coller dans Lovable, Bolt, Cursor ou votre assistant de code. »).
- **Bordure** : Filet fin discret de 1px, fond neutre très pâle (`#f5f5f4`).

### 3.7. Périmètre non testé (`ScopeBoundaries`)
- **Structure** : Liste claire et exhaustive des contrôles intentionnellement exclus du périmètre de l'offre (tests d'intrusion actifs, ingénierie sociale, audits physiques, etc.).

### 3.8. Pagination et pied de page
- Pagination : Gestion de la numérotation automatique de page via `@page` CSS (`page` / `pages`). Aucun pied de page surchargé.

---

## 4. Règles Typographiques et Rédactionnelles (Anti-Slop)

1. **Aucun tiret cadratin (`—`)** : Remplacé par deux-points (`:`), virgules (`,`), points (`.`) ou parenthèses.
2. **Aucun superlatif creux** : Proscrire tout jargon d'auto-félicitation (« révolutionnaire », « de pointe », « bulletproof »).
3. **Vérité technique intégrale** : Les versions de bibliothèques citées doivent correspondre strictement aux versions réelles vérifiées via le gestionnaire de paquets (`npm view`, `npm audit`).
4. **Pas d'en-tête répété à outrance** : L'indication des outils IA compatibles n'est formulée qu'une seule fois dans le document, au dessus du premier constat.
