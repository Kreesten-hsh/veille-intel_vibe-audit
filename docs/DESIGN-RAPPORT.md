# Système de Design : Rapports Vibe-Audit

Ce document fixe la charte visuelle, les jetons de conception (tokens), les ratios de contraste et les spécifications des composants pour les rapports d'audit de cybersécurité Vibe-Audit.

---

## 1. Principes Directeurs

1. **Format Natif : A4 Paysage (297 × 210 mm)**  
   Conçu pour une consultation sur écran d'ordinateur portable (16:9 / 16:10) sans défilement saccadé, optimisé pour l'exportation et l'impression PDF haute fidélité.
2. **Direction Hybride Distinctive**  
   - **Page 1 (Synthèse & Identité)** : Fond sombre `#0A0F20`, grandes cartes `#11182D` à bordures subtiles (`#1E293B`), et accents turquoise (`#27D3B1`) pour un impact statutaire et moderne.  
   - **Pages 2 à 6 (Lecture & Fiches Techniques)** : Fond clair reposant (`#F4F7FB`), cartes blanches (`#FFFFFF`) avec bordures douces (`#E2E8F0`), et blocs de code sombres (`#0F172A`) pour les preuves et les prompts.
3. **Formes Modernes & Hiérarchie Visuelle (Anti-Rigidité)**  
   - Grandes cartes : rayon de courbure de **14 à 18 px**.  
   - Cartes internes et sous-blocs : rayon de **8 à 12 px**.  
   - Statuts et catégories : pilules arrondies (`border-radius: 9999px`).  
   - Actions prioritaires : lignes horizontales détachées avec numérotation nette.
4. **Vérité Statistique & Séparation des Métriques**  
   - La **barre empilée de sévérité** ne représente que les vulnérabilités confirmées.  
   - Les **contrôles examinés sans anomalie** sont comptabilisés séparément dans une carte dédiée.  
   - Aucun pourcentage global arbitraire ni score synthétique bidon.
5. **Sobriété Éditoriale (Anti-Slop)**  
   - Pas de longs avertissements répétés : une pastille compacte et claire `DÉMO · application et données fictives`.  
   - Les composants hors périmètre (ex: Stripe) sont qualifiés de *« Non évalué dans cette mission »*.  
   - Les dates de capture sont strictement antérieures ou égales à l'heure d'audit, avec utilisation de domaines de documentation neutres (`leadflow-demo.example`).

---

## 2. Jetons de Conception (Design Tokens)

### 2.1. Palette Chromatique

| Jeton | Code Hex / RGBA | Usage | Rôle |
|---|---|---|---|
| `--color-dark-bg` | `#0A0F20` | Fond de page 1 (Sombre) | Immersion statutaire |
| `--color-dark-surface` | `#11182D` | Cartes Page 1 | Surface sombre |
| `--color-dark-border` | `#1E293B` | Filets Page 1 | Délimitation subtile |
| `--color-light-bg` | `#F4F7FB` | Fond des pages techniques | Confort de lecture |
| `--color-light-surface`| `#FFFFFF` | Cartes pages techniques | Surface blanche |
| `--color-light-border` | `#E2E8F0` | Filets pages techniques | Délimitation claire |
| `--color-code-surface` | `#0F172A` | Terminaux, preuves et prompts | Ardoise sombre mat |
| `--color-accent-teal` | `#27D3B1` | Accent principal tech / marque | Navigation & points clés |
| `--color-accent-cyan` | `#38BDF8` | Commandes curl & SQL | Lisibilité code |

### 2.2. Niveaux de Sévérité & Statuts (Pilules)

| Gravité | Texte | Fond | Bordure | Usage |
|---|---|---|---|---|
| **Critique** | `#B91C1C` | `#FEF2F2` | `#F87171` | Compromission totale ou fuite massive |
| **Élevé** | `#C2410C` | `#FFF7ED` | `#FDBA74` | Faille d'isolation RLS ou clé secrète |
| **Moyen** | `#B45309` | `#FEFCE8` | `#FDE047` | Configuration trop permissive |
| **Faible** | `#0369A1` | `#F0F9FF` | `#BAE6FD` | Fuite d'information mineure |
| **Conforme** | `#10B981` | `rgba(16, 185, 129, 0.12)` | `rgba(16, 185, 129, 0.3)` | Contrôle testé robuste |
| **Hors périmètre** | `#94A3B8` | `rgba(148, 163, 184, 0.12)` | `rgba(148, 163, 184, 0.25)` | Composant non évalué |

---

## 3. Typographie

- **Interface, Titres & Paragraphes** : **Inter** (400, 500, 600, 700).
- **Code, Preuves & Prompts** : **JetBrains Mono** (400, 500, 600).

### Échelle Typographique A4 Paysage
- **H1 Titre Rapport** : 19pt / 26px (Bold, tracking -0.02em).
- **H2 Titre Section / Carte** : 12.5pt / 17px (Bold, tracking 0.04em, majuscules discrètes).
- **H3 Titre Constat** : 14.5pt / 19px (Bold, tracking -0.01em).
- **Corps de texte** : 11pt / 15px (Regular, interligne 1.55).
- **Code & Commandes** : 9pt / 12px (Regular, interligne 1.45).
- **Métadonnées & Badges** : 9.5pt à 10.5pt.

---

## 4. Composants Clés

1. **Bandeau de Répartition (Page 1)** : Barre empilée (2 Élevées à 50%, 1 Moyenne à 25%, 1 Faible à 25%) flanquée de la carte autonome *4 vérifiés conformes*.
2. **Piles d'Actions Prioritaires (Page 1)** : 3 cartes horizontales à fond `#0A0F20`, badge numéroté cyan et synthèse en 2 lignes.
3. **Split-Card Constat & Prompt (Page 2)** :
   - *Volet Gauche* : Impact métier dans une carte claire avec liseré d'accent + Bloc sombre terminal compact avec en-tête `Content-Range: 0-1/142`.
   - *Volet Droit* : Prompt sombre avec liseré d'accent turquoise, mention explicite de l'hypothèse de schéma + Checklist de validation aux indicateurs neutres (`○`).
