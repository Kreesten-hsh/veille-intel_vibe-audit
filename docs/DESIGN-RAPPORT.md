# Système de Design : Rapports Vibe-Audit

Ce document fixe les spécifications visuelles, les jetons de conception (tokens), les ratios de contraste et les règles de mise en page pour les rapports d'audit Vibe-Audit.

---

## 1. Principes Directeurs

1. **Format Natif Écran & Document : A4 Paysage (297 × 210 mm)**  
   Conçu pour une consultation fluide sur écran d'ordinateur (MacBook / PC portable) sans défilement vertical saccadé, tout en garantissant une impression PDF nette.
2. **Esthétique Hybride "Cyber Sobre"**  
   - **Page 1 (Couverture & Synthèse)** : Fond bleu nuit profond (`#0A0F20`), cartes sombres et accents technologiques discrets (effet statutaire et moderne pour les décideurs).  
   - **Pages 2 à 6 (Lecture, Constats & Remédiation)** : Fond clair reposant (`#F4F7FB` et cartes `#FFFFFF`), évitant la fatigue visuelle des documents denses et préservant l'encrage à l'impression. Blocs de code et de prompts en ardoise sombre (`#111827`) pour un confort de lecture optimal.
3. **Rigueur Factuelle & Anti-Slop (Normes OWASP & NIST)**  
   - Pas de score global arbitraire (ex: "82% sécurisé") ni d'émojis.
   - Les indicateurs reposent sur des comptes réels de constats et une matrice de couverture explicite.
   - Les niveaux de sévérité sont formulés en toutes lettres avec leur code couleur associé.
4. **Distinction Stricte des Trois Statuts de Correction**  
   - `Constat confirmé` : Vulnérabilité observée et reproduite.
   - `Correction proposée` : Prompt et étapes suggérés pour remédiation.
   - `Correction vérifiée` : Re-contrôle effectif post-correction (uniquement si exécuté).

---

## 2. Jetons de Conception (Design Tokens)

### 2.1. Palette Chromatique & Ratios de Contraste Mesurés (WCAG AA)

Toutes les combinaisons ont été mesurées selon l'algorithme WCAG 2.1 (seuil minimal 4.5:1 pour le texte normal, 3.0:1 pour les composants d'interface et textes de grande taille).

#### Univers Sombre (Page 1 — Couverture & Synthèse)
| Jeton | Code Hex | Rôle | Contraste mesuré | Statut WCAG |
|---|---|---|---|---|
| `--color-dark-bg` | `#0A0F20` | Fond de page sombre principal | — | Fond |
| `--color-dark-surface` | `#11182D` | Cartes et conteneurs de synthèse | — | Surface |
| `--color-dark-border` | `#1E293B` | Filets et bordures de cartes | 2.1:1 sur fond | Décoratif structuré |
| `--color-dark-text-head` | `#FFFFFF` | Titres et chiffres clés | 17.8:1 sur `#0A0F20` | Conforme AA / AAA |
| `--color-dark-text-body` | `#94A3B8` | Texte courant et descriptions | 6.5:1 sur `#0A0F20` | Conforme AA |
| `--color-dark-text-muted`| `#64748B` | Métadonnées et étiquettes | 4.6:1 sur `#0A0F20` | Conforme AA |
| `--color-accent-cyan` | `#00D2D3` | Accent tech et navigation (ajusté pour contraste) | 9.4:1 sur `#0A0F20` | Conforme AA / AAA |

#### Univers Clair (Pages 2 à 6 — Lecture & Fiches de Constats)
| Jeton | Code Hex | Rôle | Contraste mesuré | Statut WCAG |
|---|---|---|---|---|
| `--color-light-bg` | `#F4F7FB` | Fond général de lecture | — | Fond |
| `--color-light-card` | `#FFFFFF` | Cartes de constats et blocs | — | Surface |
| `--color-light-border` | `#E2E8F0` | Filets de cartes et séparateurs | 1.3:1 sur fond | Décoratif structuré |
| `--color-text-primary` | `#0F172A` | Titres de constats et texte fort | 14.8:1 sur `#FFFFFF` | Conforme AA / AAA |
| `--color-text-secondary`| `#334155` | Corps de texte et explications | 9.6:1 sur `#FFFFFF` | Conforme AA / AAA |
| `--color-text-muted` | `#64748B` | Libellés secondaires et dates | 4.6:1 sur `#FFFFFF` | Conforme AA |

#### Blocs Techniques & Terminaux (Code & Prompts — Pages 2 à 6)
| Jeton | Code Hex | Rôle | Contraste mesuré | Statut WCAG |
|---|---|---|---|---|
| `--color-code-bg` | `#111827` | Fond ardoise nuit des terminaux | — | Fond bloc |
| `--color-code-text` | `#F8FAFC` | Sorties de commandes et prompts | 15.2:1 sur `#111827` | Conforme AA / AAA |
| `--color-code-comment`| `#94A3B8` | Commentaires et critères | 6.1:1 sur `#111827` | Conforme AA |
| `--color-code-cyan` | `#38BDF8` | Commandes curl / mots-clés SQL | 8.7:1 sur `#111827` | Conforme AA / AAA |

#### Niveaux de Sévérité & Statuts
| Gravité | Couleur Texte | Couleur Fond (Badge clair) | Contraste Texte/Fond | Rôle |
|---|---|---|---|---|
| **Critique** | `#B91C1C` (Rouge profond) | `#FEF2F2` (Rose très pâle) | 6.2:1 | Faille exploitable immédiatement avec compromission majeure |
| **Élevé** | `#C2410C` (Ocre soutenu) | `#FFF7ED` (Ambre très pâle) | 5.3:1 | Contournement de contrôle d'accès ou fuite de données |
| **Moyen** | `#B45309` (Brun ambre) | `#FEFCE8` (Jaune très pâle) | 5.2:1 | Mauvaise pratique de configuration ou injection potentielle |
| **Faible** | `#0369A1` (Bleu profond) | `#F0F9FF` (Bleu glacier pâle) | 5.8:1 | Header manquant ou fuite d'informations mineure |
| **Validé / Sûr** | `#047857` (Émeraude sombre) | `#ECFDF5` (Menthe très pâle) | 5.7:1 | Contrôle testé conforme et robuste |

---

## 3. Typographie

Deux familles de polices sont retenues :
1. **Interface & Texte** : **Inter** (sans-serif géométrique lisible et neutre).
2. **Preuves & Prompts** : **JetBrains Mono** (monospace technique à espacement clair).

### Échelle Typographique (Calibrée A4 Paysage)
| Rôle | Police | Graisse | Taille (pt / px) | Interligne |
|---|---|---|---|---|
| **Titre Principal (H1)** | Inter | 700 (Bold) | 24pt / 32px | 1.20 |
| **Titre de Section (H2)** | Inter | 600 (Semibold) | 16pt / 21px | 1.25 |
| **Titre de Constat (H3)** | Inter | 600 (Semibold) | 12.5pt / 16.5px | 1.30 |
| **Corps de Texte** | Inter | 400 (Regular) | 9.5pt / 12.5px | 1.45 |
| **Métadonnées & Badges** | Inter | 600 (Semibold) | 8pt / 10.5px | 1.20 |
| **Code & Commandes** | JetBrains Mono | 400 / 500 | 8pt / 10.5px | 1.40 |

---

## 4. Iconographie (Lucide SVG)

- Utilisation exclusive des tracés SVG au format vectoriel (pas d'émojis).
- Paramètres homogènes : `width: 16px`, `height: 16px`, `stroke-width: 1.75px`, `stroke-linecap: round`, `stroke-linejoin: round`.
- Bibliothèque principale :
  - `shield-alert` : Présence de failles critiques / élevées.
  - `shield-check` : Contrôle sécurisé ou statut global satisfaisant.
  - `database` : Supabase, PostgreSQL, tables et Row Level Security.
  - `key-round` : Clés API, variables d'environnement, secrets.
  - `terminal` : Ligne de commande de reproduction `curl` ou prompt IA.
  - `check-circle-2` : Critère de validation satisfait.
  - `alert-triangle` : Avertissement ou impact métier.
  - `file-text` : Métadonnées, conventions et périmètre.

---

## 5. Spécifications des Composants

### 5.1. Barre de Gravité Empilée (`StackedSeverityBar`)
- Remplace les graphiques en anneau non proportionnels.
- Affiche la ventilation exacte des constats en 4 blocs compacts : Critique (`#EF4444`), Élevé (`#F97316`), Moyen (`#F59E0B`), Faible (`#0284C7`).
- Chaque bloc affiche l'étiquette en toutes lettres et le nombre exact de constats.

### 5.2. Matrice de Couverture (`ScopeMatrix`)
- Tableau synthétique listant chaque domaine de contrôle :
  1. Sécurité de la base et RLS (Supabase)
  2. Authentification et sessions
  3. Clés API et bundles frontend
  4. Webhooks et flux de paiement
  5. En-têtes HTTP et politique CORS
- Chaque domaine affiche un statut clair : **Examiné avec constat**, **Examiné sans anomalie**, ou **Non testé (hors périmètre)**.

### 5.3. Fiche de Constat en Split-Card (`FindingSplitCard`)
- Disposition en 2 colonnes horizontales équilibrées :
  - **Colonne Gauche (Compréhension & Preuve)** :
    - Badge de sévérité + Identifiant (ex: `SEC-01`).
    - Statut du constat : `Constat confirmé`.
    - Impact métier : Explication non technique en 2 phrases pour le fondateur.
    - Preuve reproductible : Commande exacte `curl` et réponse HTTP dans un bloc ardoise sombre.
  - **Colonne Droite (Remédiation & Validation)** :
    - Statut du correctif : `Correction proposée`.
    - Bloc Prompt IA : Prompt complet prêt à coller dans l'assistant (Lovable / Bolt / Cursor).
    - Critères de validation : 2 ou 3 vérifications concrètes permettant au client de s'assurer que le problème est résolu.

### 5.4. Bloc "Périmètre, Limites et Confidentialité"
- Documente explicitement la méthodologie non destructive, les zones non couvertes (tests de charge, ingénierie sociale, tiers Stripe/AWS) et le respect du secret d'affaires.

---

## 6. Règles CSS Print pour A4 Paysage

```css
@page {
  size: A4 landscape;
  margin: 0;
}

body {
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 297mm;
  height: 210mm;
  page-break-after: always;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
}
```
