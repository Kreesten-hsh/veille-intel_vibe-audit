# PLAN D'ACTION CONCRET : JOUR PAR JOUR JUSQU'AU 31 DÉCEMBRE 2026
*Objectif absolu : Encaisser 2 000 000 FCFA (~3 049 €) sur compte bancaire (plancher vital : 1 000 000 FCFA).*

---

## 0. LES 4 RÈGLES D'OR DE L'OPÉRATEUR

1. **ZÉRO APPEL TÉLÉPHONIQUE OU VISIO** :
   Toute la prospection, la négociation, la livraison et le suivi se font **100% par écrit** (Email direct et messagerie LinkedIn / X). Zéro temps perdu en réunions ou qualifications orales.
2. **AUCUN ENVOI AUTOMATIQUE DE MASSE** :
   Chaque message est envoyé manuellement un par un, avec une personnalisation chirurgicale (nom du dirigeant, client réel cité sur leur site, concurrents réels ou détail technique de l'app).
3. **ZÉRO DÉPENSE SUPPLÉMENTAIRE** :
   Aucun outil payant, aucun abonnement supplémentaire (respect strict de `docs/02-OUTILS.md`).
4. **DISCIPLINE MILITAIRE (2 BLOCS PAR JOUR)** :
   - **Matin (09h00 - 11h30)** : **Veille-Intel** (10 emails manuels personnalisés avec `output/veille-sample-report.pdf` en pièce jointe).
   - **Après-midi (14h00 - 16h30)** : **Vibe-Audit** (5 prises de contact directes ciblées + relances J+3/J+7).

---

## 1. STRATÉGIE COMMERCIALE OPTIMISÉE (ZÉRO SUR-INGÉNIERIE)

### Pipeline 1 : Veille-Intel (399 € / mois en Marque Blanche)
- **Le modèle "Pull" (Zéro travail dans le vide)** :
  - **J0 (Prise de contact)** : On envoie un email court et direct au dirigeant d'agence. On cite un vrai client de son agence et 2 concurrents directs de ce client. On attache `output/veille-sample-report.pdf` pour prouver immédiatement la qualité du livrable exécutif de 4 pages.
  - **L'offre d'accroche irrésistible** : « Répondez simplement "GO" et je vous génère gratuitement l'édition n°1 sur ces 2 concurrents sous 24h, prête à transférer à votre client lundi prochain à vos couleurs ».
  - **L'effort de production sur mesure** : Réalisé **uniquement** pour les agences qui répondent favorablement. Zéro rapport sur mesure rédigé dans le vide pour des prospects froids.
  - **Conversion au paiement** : À la livraison de l'édition d'essai gratuite, envoi de la proposition pour l'abonnement mensuel récurrent à 399 € / mois (garantie satisfait ou remboursé le 1er mois).

### Pipeline 2 : Vibe-Audit (Pilote 99 € / Standard 249 € + Upsell PR 150-250 €)
- **Prise de contact ciblée** : Détection des créateurs ayant annoncé un SaaS avec Lovable, Bolt, Cursor ou Supabase.
- **Accroche bienveillante** : Félicitations pour le produit + mise en garde technique concrète (RLS Supabase, secrets API exposés côté client). Proposition de l'un des 2 spots pilotes à 99 € contre témoignage écrit.
- **Protocole de sécurisation** : Signature préalable de l'accord de confidentialité et consentement (`templates/vibe-audit/accord-consentement.md`).
- **Livraison sous 48h** : Rapport PDF généré (`output/leadflow-report.pdf`) avec prompts de remédiation clé en main.
- **L'Accélérateur de Revenus (Option Upsell)** :
  Systématiquement lors de la livraison du rapport, proposer l'option :
  *« Si vous manquez de temps pour appliquer les correctifs, je peux implémenter directement les corrections via une Pull Request sécurisée et testée sous 24h sur votre dépôt GitHub pour +150 € (offre pilote) ou +250 € (standard). »*
  ➔ Transforme un ticket de 99 € en 249 €, et un ticket de 249 € en 499 €, doublant la vitesse d'encaissement.

---

## 2. CALENDRIER OPÉRATIONNEL IMMÉDIAT (DU 14 OCTOBRE AU 31 DÉCEMBRE 2026)

### SEMAINE 1 : DU MERCREDI 14 AU DIMANCHE 18 OCTOBRE (ACTION IMMÉDIATE)

#### Mercredi 14 Octobre (AUJOURD'HUI - DÉMARRAGE DE LA PROSPECTION) :
- [ ] **Matin (Veille-Intel)** :
  - Envoyer les 10 premiers emails personnalisés aux 10 agences qualifiées (`output/MESSAGES_PRETS_AUJOURDHUI.md`) avec `output/veille-sample-report.pdf` en pièce jointe.
  - Enregistrer les envois dans [`docs/PROSPECTS.csv`](file:///home/hasashi/Bureau/veille-intel_vibe-audit/docs/PROSPECTS.csv).
- [ ] **Après-midi (Vibe-Audit)** :
  - Envoyer les 4 relances immédiates aux prospects contactés le 9 octobre (François Gaquere, Nicolas Gilquin, Flavie Prévot, Camel Dagbegnon).
  - Envoyer les 5 premiers messages directs ciblés (Romain Pires, Antoine Fallot, Maxence Vroilant, Jan-Kasper Jakubowski, Hélène).

#### Jeudi 15 Octobre :
- [ ] **Matin (Veille-Intel)** :
  - Traiter les premières réponses "GO" des agences : générer leur rapport d'essai gratuit sur les 2 concurrents cités via `scripts/capture.py` et `scripts/render_report.py`.
  - Sourcer 5 nouvelles agences à Nantes et Bordeaux.
- [ ] **Après-midi (Vibe-Audit)** :
  - Traiter les retours des créateurs. Envoi du lien d'accord de consentement pour tout accord de principe.
  - Contacter 5 nouveaux créateurs d'apps repérés sur X / Product Hunt / Cube.

#### Vendredi 16 Octobre (J+2 Relance & Suivi) :
- [ ] **Matin (Veille-Intel)** :
  - Envoyer 10 nouveaux emails personnalisés d'attaque.
  - Livrer les rapports d'essai aux agences ayant répondu jeudi.
- [ ] **Après-midi (Vibe-Audit)** :
  - Verrouiller et faire signer le **1er client pilote à 99 €** (émission de la facture via `docs/FACTURE-TEMPLATE.md`).
  - Lancer le scan technique passif dès réception du consentement signé.

#### Samedi 17 - Dimanche 18 Octobre :
- [ ] **Livraison du 1er audit pilote** sous 48h (avec option Upsell PR à +150 €).
- [ ] Préparation des 10 cibles Veille-Intel pour le lundi matin.

---

### SEMAINE 2 : DU 19 AU 25 OCTOBRE (PREMIER POINT D'ARRÊT CRITIQUE)

#### Lundi 19 Octobre :
- [ ] **Matin** : 10 emails d'attaque `veille-intel` + relance douce (J+5) des agences contactées le 14 octobre sans réponse.
- [ ] **Après-midi** : 5 nouveaux messages `vibe-audit` + proposition de l'upsell au premier client livré.

#### Mardi 20 au Jeudi 22 Octobre :
- [ ] Poursuivre le rythme strict : 10 emails Veille-Intel le matin, 5 contacts Vibe-Audit l'après-midi.
- [ ] Signer et encaisser le **2e client pilote Vibe-Audit (99 €)**.

#### Vendredi 23 - Samedi 24 Octobre (POINT D'ARRÊT N°1 - JALON OFFICIEL) :
- [ ] **Bilan chiffré des 10 premiers jours** :
  - Total contacts Veille-Intel : ~50 agences contactées ➔ Objectif : au moins 5 réponses positives et 2 rapports d'essai livrés.
  - Total contacts Vibe-Audit : ~25 créateurs contactés ➔ Objectif : au moins 2 pilotes vendus (**198 € encaissés = ~130 000 FCFA**) + 1er témoignage écrit récupéré.

---

### SEMAINE 3 : DU 26 AU 31 OCTOBRE (CONVERSION DES PREMIÈRES AGENCES)

- [ ] **Veille-Intel** : Transformer les 2 agences convaincues par l'essai gratuit en abonnements fermes à 399 € / mois pour démarrage officiel début novembre.
- [ ] **Vibe-Audit** : Fin de l'offre pilote. Passage au tarif officiel de **249 €** (avec les 2 témoignages des pilotes comme preuve sociale).
- [ ] **Objectif fin octobre** : Encaisser les acomptes ou premiers abonnements.

---

### SEMAINE 4 : DU 02 AU 10 NOVEMBRE (LE VERROUILLAGE DES DEUX MILLIONS)

> [!IMPORTANT]
> **DATE BUTOIR STRATÉGIQUE (10 NOVEMBRE)** :
> Tout abonnement Veille-Intel débutant avant le 10 novembre encaisse 2 mensualités pleines avant le 31 décembre (Novembre + Décembre).

#### Objectifs fermes au 10 Novembre :
- [ ] **Veille-Intel** : **2 abonnements confirmés et payés** (2 × 399 € = **798 € = 523 000 FCFA**).
- [ ] **Vibe-Audit** : **2 pilotes encaissés (198 €)** + **2 audits standards à 249 € (498 €)** = **696 € (~456 000 FCFA)**.
- [ ] **TOTAL ENCAISSÉ AU 10 NOVEMBRE** : **1 494 € (~979 000 FCFA)** ➔ **Le plancher vital de 1 Million FCFA est franchi !**

---

### DU 11 NOVEMBRE AU 31 DÉCEMBRE (L'ATTEINTE DES 2 MILLIONS FCFA)

- **Production récurrente Veille-Intel** : Chaque lundi matin à 08h00, génération et livraison des 2 rapports hebdomadaires aux agences (45 min par rapport).
- **Renouvellement Mois 2 (Décembre)** : Deuxième encaissement automatique des 2 agences (**798 €**).
- **Ventes Vibe-Audit (Novembre & Décembre)** : Réaliser 3 à 4 audits supplémentaires à 249 € + 2 options d'implémentation de correctifs à +200 €.

---

## 3. TABLEAU DE BORD DE RÉUSSITE FINANCIÈRE AU 31 DÉCEMBRE 2026

| Source de Revenus | Ventes Concrètes Réalisées | Cash Reçu en Euros | Cash Reçu en FCFA |
| :--- | :--- | ---: | ---: |
| **Veille-Intel (Agence 1)** | Mensualités Novembre + Décembre | 798 € | 523 453 FCFA |
| **Veille-Intel (Agence 2)** | Mensualités Novembre + Décembre | 798 € | 523 453 FCFA |
| **Vibe-Audit (Pilotes)** | 2 audits initiaux (99 €) | 198 € | 129 880 FCFA |
| **Vibe-Audit (Standards)** | 5 audits complets 48h (249 €) | 1 245 € | 816 666 FCFA |
| **Vibe-Audit (Upsells PR)** | 2 options implémentation correctifs (150 €) | 300 € | 196 787 FCFA |
| **TOTAL GÉNÉRAL NET** | **9 clients au total** | **3 339 €** | **2 190 239 FCFA** |

**➔ OBJECTIF DE 2 000 000 FCFA DÉPASSÉ DÈS DÉCEMBRE SANS AUCUN APPEL, SANS MASSE ET SANS FRAIS.**
