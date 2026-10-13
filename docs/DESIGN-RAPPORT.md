# Système de Design : Rapports Vibe-Audit

Ce document fixe les spécifications visuelles, les jetons de conception (tokens), les ratios de contraste et les règles de mise en page pour les rapports d'audit Vibe-Audit.

---

## 1. Principes Directeurs

1. **Format Natif Écran & Document : A4 Paysage (297 × 210 mm)**  
   Conçu pour une consultation fluide sur écran d'ordinateur (MacBook / PC portable) sans défilement vertical saccadé, tout en garantissant un export PDF haute fidélité.
2. **Couleur de Fond Unifiée : Univers Sombre (`#0A0F20`) sur Toutes les Pages**  
   - Toutes les pages partagent le même fond spatial sombre profond (`#0A0F20`) pour une identité de marque cohérente, statutaire et immersive du début à la fin du document.  
   - Cartes et panneaux en surface sombre (`#11182D`) délimitées par des filets gris ardoise discrets (`#1E293B`).  
   - Terminaux, blocs de preuves et de prompts en ardoise ultra-sombre (`#060A14` ou `#0F172A`).  
   - Textes à contraste élevé conforme WCAG AA : titres en blanc pur (`#FFFFFF`), corps de texte en slate clair (`#CBD5E1` et `#94A3B8`).
3. **Séparation Stricte des Unités & Vérité Statistique**  
   - La **barre empilée de gravité** comptabilise exclusivement les vulnérabilités confirmées (Critique, Élevé, Moyen, Faible).  
   - Les **contrôles examinés sans anomalie** font l'objet d'un compteur ou d'une carte séparée pour ne jamais mélanger failles et conformités dans une même barre proportionnelle.  
   - Aucun score arbitraire global (ex: "82% sécurisé") ni émojis.
4. **Cohérence du Périmètre & Traçabilité Réelle (NIST SP 800-115)**  
   - Tout composant hors périmètre (ex: Stripe) est explicitement qualifié de *« Non évalué (hors périmètre) »* et n'est jamais déclaré "sain" ou "sécurisé".  
   - Chaque preuve technique indique le contexte de capture : horodatage UTC, méthode HTTP, type de clé utilisé et preuve tangible de dénombrement (en-tête `Content-Range`).
5. **Neutralité des Statuts de Validation Post-Correction**  
   - Une correction suggérée porte le statut `Correction proposée`.  
   - Les critères de validation affichent des indicateurs neutres (cases à cocher / cercles vides) symbolisant les actions restant à exécuter par le développeur. La couleur verte est réservée aux contrôles réellement vérifiés.
6. **Encadré de Démonstration Obligatoire pour les Échantillons Commerciaux**  
   Tout échantillon ou démonstrateur commercial doit afficher un avertissement explicite stipulant que les données et la cible sont fictives, opérées dans un environnement de test contrôlé (sandbox).

---

## 2. Jetons de Conception (Design Tokens)

### 2.1. Palette Chromatique Unifiée (Fond Sombre `#0A0F20`)

Toutes les combinaisons respectent les exigences WCAG 2.1 AA (contraste minimal de 4.5:1 pour le texte normal, 3.0:1 pour les composants d'interface).

| Jeton | Code Hex | Rôle | Contraste mesuré | Statut WCAG |
|---|---|---|---|---|
| `--color-bg-base` | `#0A0F20` | Fond principal de toutes les pages | — | Base de fond |
| `--color-surface-card` | `#11182D` | Cartes, split-cards et panneaux | — | Surface carte |
| `--color-surface-code` | `#0A101D` | Blocs terminaux, preuves et prompts | — | Surface code |
| `--color-border-subtle` | `#1E293B` | Filets délimitant les cartes | 2.1:1 sur fond | Décoratif structuré |
| `--color-border-accent` | `#334155` | Bordures actives et séparateurs | 3.2:1 sur fond | Conforme UI |
| `--color-text-heading` | `#FFFFFF` | Titres majeurs et chiffres clés | 17.8:1 sur `#0A0F20` | Conforme AAA |
| `--color-text-body` | `#CBD5E1` | Corps de texte et descriptions | 11.2:1 sur `#0A0F20` | Conforme AAA |
| `--color-text-muted` | `#94A3B8` | Métadonnées, labels secondaires | 6.5:1 sur `#0A0F20` | Conforme AA |
| `--color-accent-cyan` | `#00D2D3` | Accent tech et navigation | 9.4:1 sur `#0A0F20` | Conforme AAA |

### 2.2. Niveaux de Sévérité & Statuts

| Gravité | Couleur Accent | Couleur Fond Badge | Contraste Texte/Fond | Rôle |
|---|---|---|---|---|
| **Critique** | `#EF4444` (Rouge vif) | `rgba(239, 68, 68, 0.15)` | 7.4:1 sur fond sombre | Compromission immédiate ou fuite massive |
| **Élevé** | `#F97316` (Ambre soutenu) | `rgba(249, 115, 22, 0.15)` | 6.8:1 sur fond sombre | Faille d'isolation ou clé secrète exposée |
| **Moyen** | `#F59E0B` (Jaune cyber) | `rgba(245, 158, 11, 0.15)` | 8.2:1 sur fond sombre | Configuration permissive ou header manquant |
| **Faible** | `#0284C7` (Bleu ciel) | `rgba(2, 132, 199, 0.15)` | 5.9:1 sur fond sombre | Divulgation mineure d'information |
| **Contrôle Sécurisé** | `#10B981` (Émeraude) | `rgba(16, 185, 129, 0.15)` | 6.7:1 sur fond sombre | Contrôle testé conforme et robuste |

---

## 3. Typographie

- **Interface & Contenu** : **Inter** (sans-serif géométrique lisible et neutre).
- **Code, Preuves & Prompts** : **JetBrains Mono** (monospace technique avec espacement rigoureux).

### Échelle Typographique A4 Paysage
| Rôle | Police | Graisse | Taille (pt / px) | Interligne |
|---|---|---|---|---|
| **Titre Principal (H1)** | Inter | 700 (Bold) | 22pt / 28px | 1.20 |
| **Titre de Section (H2)** | Inter | 600 (Semibold) | 15pt / 20px | 1.25 |
| **Titre de Constat (H3)** | Inter | 600 (Semibold) | 12pt / 16px | 1.30 |
| **Corps de Texte** | Inter | 400 (Regular) | 9.5pt / 12.5px | 1.45 |
| **Métadonnées & Badges** | Inter | 600 (Semibold) | 8pt / 10.5px | 1.20 |
| **Code & Commandes** | JetBrains Mono | 400 / 500 | 8pt / 10.5px | 1.40 |

---

## 4. Iconographie (Lucide SVG)

- Tracés vectoriels SVG fins (`stroke-width: 1.75px`), sans emojis.
- `shield-alert` / `shield-check` : Statut global et contrôles vérifiés.
- `database` : Supabase, bases SQL et configurations RLS.
- `terminal` : Ligne de commande passive et prompts IA.
- `circle` / `square` (tracés neutres non cochés) : Critères de validation post-correction restant à effectuer.
- `alert-triangle` : Impact métier et avertissements de sécurité.

---

## 5. Composants Graphiques

1. **Barre de Gravité Empilée (`StackedSeverityBar`)** :
   - N'intègre que les vulnérabilités réelles (ex: 2 Élevés, 1 Moyen, 1 Faible = 4 constats au total).
   - Carte adjacente dédiée : *Contrôles examinés sans anomalie : 4*.
2. **Bandeau de Démonstration (`DemoBanner`)** :
   - Présent sur tout échantillon commercial pour dissiper toute ambiguïté sur l'origine des données.
3. **Split-Card Constat & Prompt** :
   - Gauche : Impact métier vulgarisé + Preuve technique reproductible (`curl -i` avec en-tête `Content-Range: 0-1/142`, date UTC et méthode).
   - Droite : Badge `Correction proposée` + Prompt IA avec hypothèses d'architecture documentées + Checklist de validation aux icônes neutres.
