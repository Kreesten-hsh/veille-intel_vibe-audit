# Modélisation Financière, Calendrier d'Encaissement & Scénarios

> **Avertissement méthodologique :** Aucun taux de conversion n'est présenté comme un fait acquis. Tous les ratios commerciaux sont explicitement qualifiés d'**« hypothèses »** et associés à des formules de calcul visibles. Les montants ne comptabilisent que les fonds réellement encaissés sur compte bancaire avant le 31 décembre 2026.

---

## 1. Paramètres Fondamentaux & Taux de Change

- **Taux de change fixe officiel de référence :** $1\text{ €} = 655,957\text{ FCFA}$.
- **Objectifs financiers au 31 décembre 2026 :**
  - **Plancher financier :** $1\,000\,000\text{ FCFA}$
    $$\text{Plancher en €} = \frac{1\,000\,000\text{ FCFA}}{655,957\text{ FCFA/€}} = 1\,524,49\text{ €}$$
  - **Cible financière :** $2\,000\,000\text{ FCFA}$
    $$\text{Cible en €} = \frac{2\,000\,000\text{ FCFA}}{655,957\text{ FCFA/€}} = 3\,048,98\text{ €}$$

### Grille Tarifaire Unitaire
- **Veille-Intel (Abonnement mensuel) :**
  - Tarif Pionnier ($P_{\text{veille,1}}$) : **399,00 € / mois** (3 premiers clients).
  - Tarif Standard ($P_{\text{veille,2}}$) : **499,00 € / mois** (à partir du 4ᵉ client).
- **Vibe-Audit (Forfait ponctuel) :**
  - Tarif Pilote ($P_{\text{audit,pilote}}$) : **99,00 €** (2 premiers clients).
  - Tarif Standard ($P_{\text{audit,std}}$) : **249,00 €**.
  - Tarif Restitution ($P_{\text{audit,rest}}$) : **399,00 €**.

---

## 2. Formule des Mensualités / Ventes Nécessaires

La formule de calcul du nombre d'unités de facturation nécessaires pour atteindre un objectif est :
$$\text{Nombre d'unités nécessaires} = \left\lceil \frac{\text{Objectif en €}}{\text{Prix unitaire en €}} \right\rceil$$

### 2.1 Pour le Plancher Financier (1 524,49 € / 1 000 000 FCFA)

| Offre isolée | Prix retenu | Formule de calcul | Unités nécessaires | Total encaissé en € | Total encaissé en FCFA |
| :--- | :---: | :--- | :---: | :---: | :---: |
| **Veille-Intel seul** | 399 € | $\lceil 1\,524,49 / 399 \rceil = \lceil 3,82 \rceil$ | **4 mensualités** | 1 596,00 € | 1 046 907 FCFA |
| **Vibe-Audit seul** (Mix pilote + standard) | 2 pilotes (99 €) + std (249 €) | $2 \times 99\text{ €} + \lceil (1\,524,49 - 198) / 249 \rceil \times 249\text{ €}$ $= 198\text{ €} + \lceil 5,33 \rceil \times 249\text{ €}$ | **2 pilotes + 6 standards (8 ventes)** | 1 692,00 € | 1 109 879 FCFA |

### 2.2 Pour la Cible Financière (3 048,98 € / 2 000 000 FCFA)

| Offre isolée | Prix retenu | Formule de calcul | Unités nécessaires | Total encaissé en € | Total encaissé en FCFA |
| :--- | :---: | :--- | :---: | :---: | :---: |
| **Veille-Intel seul** | 399 € / 499 € | $\lceil 3\,048,98 / 399 \rceil = \lceil 7,64 \rceil$ | **8 mensualités** (ou 7 à 499 €) | 3 192,00 € | 2 093 815 FCFA |
| **Vibe-Audit seul** | 249 € standard | $2 \times 99\text{ €} + \lceil (3\,048,98 - 198) / 249 \rceil \times 249\text{ €}$ $= 198\text{ €} + \lceil 11,45 \rceil \times 249\text{ €}$ | **2 pilotes + 12 standards (14 ventes)** | 3 186,00 € | 2 089 881 FCFA |

*(Note : Comme établi dans `docs/00-CONTEXTE.md`, viser 14 clients Vibe-Audit en solo d'ici fin décembre est qualifié de non réaliste. La cible de 2 M FCFA s'atteint par la combinaison des deux projets ou par Veille-Intel s'il survit au Gate 1).*

---

## 3. Règle de Calendrier & Impact sur les Abonnements

### Règle d'Encaissement au 31/12/2026
> **Principe :** Un client dont le premier paiement tombe le jour $J$ paie chaque mois à la même date calendaire $J$. L'encaissé au 31/12/2026 compte uniquement les paiements reçus au plus tard le 31 décembre 2026.
> 
> **Règle stricte du 17 novembre :** Tout premier encaissement intervenant après le 17 novembre 2026 ne génère **qu'un seul paiement** avant le 31 décembre 2026.

### Matrice du Nombre de Mensualités Réceptionnées par Date de Signature

| Date du 1er Paiement ($J$) | Échéances encaissées avant le 31/12/2026 | Nombre d'échéances | Valeur cumulée par client (à 399 €) |
| :--- | :--- | :---: | :---: |
| **Entre le 10/10 et le 31/10** | Jour $J$ en octobre, Jour $J$ en novembre, Jour $J$ en décembre | **3 mensualités** | 1 197,00 € (785 181 FCFA) |
| **Entre le 01/11 et le 17/11** | Jour $J$ en novembre, Jour $J$ en décembre | **2 mensualités** | 798,00 € (523 454 FCFA) |
| **Après le 17/11 (ex. 25/11 ou 05/12)** | Jour $J$ uniquement | **1 mensualité** | 399,00 € (261 727 FCFA) |

---

## 4. Calendrier de Signatures Requis pour Atteindre les Paliers

### 4.1 Atteinte du Plancher (1 000 000 FCFA / 1 525 €)

Pour atteindre le plancher avec Veille-Intel seul en respectant la règle de calendrier :
- **Condition minimale impérative :** Signer au minimum **2 agences clientes avant le 17 novembre 2026**.
  $$\text{Total encaissé} = 2\text{ clients} \times 2\text{ mensualités} \times 399\text{ €} = 1\,596,00\text{ €} \quad (1\,046\,907\text{ FCFA})$$
- Si 1 seul client est signé le 10 novembre : il ne rapporte que $2 \times 399 = 798\text{ €}$. Il manque alors $726,49\text{ €}$, nécessitant obligatoirement soit 2 nouveaux clients Veille signés après le 17 novembre ($2 \times 399 = 798\text{ €}$), soit le complément par Vibe-Audit (ex. 1 pilote à 99 € + 3 audits standards à 249 € = 846 €).

### 4.2 Atteinte de la Cible (2 000 000 FCFA / 3 049 €)

Scénario combiné équilibré :
- **Veille-Intel :** 2 agences signées avant le 10 novembre $\rightarrow$ $2 \times 2\text{ mois} \times 399\text{ €} = 1\,596,00\text{ €}$
- **Vibe-Audit :**
  - 2 pilotes signés en octobre $\rightarrow$ $2 \times 99\text{ €} = 198,00\text{ €}$
  - 5 audits standards signés entre novembre et décembre $\rightarrow$ $5 \times 249\text{ €} = 1\,245,00\text{ €}$
- **Total combiné :** $1\,596\text{ €} + 198\text{ €} + 1\,245\text{ €} = 3\,039,00\text{ €} \quad (1\,993\,453\text{ FCFA} \approx 2\text{ M FCFA})$.

---

## 5. Scénarios Commerciaux Fondés sur des Taux d'Hypothèse

Soit un volume cible de prospection de $N = 250$ contacts qualifiés par projet.
La formule en entonnoir est :
$$\text{Ventes} = N \times T_{\text{réponse}} \times T_{\text{appel}} \times T_{\text{closing}}$$

### 5.1 Scénarios pour Veille-Intel ($N = 250$ agences contactées)

| Paramètre | Scénario Prudent (Hypothèse) | Scénario de Base (Hypothèse) | Scénario Optimiste (Hypothèse) |
| :--- | :---: | :---: | :---: |
| **Taux de réponse ($T_{\text{rép}}$)** | 3,0 % (7 réponses) | 5,0 % (12 réponses) | 8,0 % (20 réponses) |
| **Taux de conversion en appel ($T_{\text{appel}}$)** | 30 % (2 appels) | 40 % (5 appels) | 50 % (10 appels) |
| **Taux de signature en appel ($T_{\text{clos}}$)** | 25 % | 40 % | 50 % |
| **Clients signés ($C$)** | $\lfloor 2 \times 0,25 \rfloor = \mathbf{0\text{ à }1\text{ client}}$ | $\lfloor 5 \times 0,40 \rfloor = \mathbf{2\text{ clients}}$ | $\lfloor 10 \times 0,50 \rfloor = \mathbf{5\text{ clients}}$ |
| **Date estimée des signatures** | Fin novembre | Mi-novembre (avant le 17/11) | Début novembre |
| **Mensualités encaissées au 31/12** | 1 mensualité (si 1 client) | $2\text{ clients} \times 2\text{ mois} = 4\text{ mensualités}$ | $3\text{ clients} \times 2\text{ mois} + 2 \times 1\text{ mois} = 8\text{ mensualités}$ |
| **Revenu total encaissé (€)** | **399,00 €** | **1 596,00 €** | **3 192,00 €** |
| **Revenu total en FCFA** | **261 727 FCFA** | **1 046 907 FCFA** *(Plancher atteint)* | **2 093 815 FCFA** *(Cible atteinte)* |

### 5.2 Scénarios pour Vibe-Audit ($N = 250$ fondateurs contactés)

| Paramètre | Scénario Prudent (Hypothèse) | Scénario de Base (Hypothèse) | Scénario Optimiste (Hypothèse) |
| :--- | :---: | :---: | :---: |
| **Taux de réponse ($T_{\text{rép}}$)** | 2,5 % (6 réponses) | 6,0 % (15 réponses) | 10,0 % (25 réponses) |
| **Taux d'accord pour audit ($T_{\text{accord}}$)** | 30 % (2 accords) | 40 % (6 accords) | 45 % (11 accords) |
| **Missions réalisées** | 2 pilotes (99 €) | 2 pilotes (99 €) + 4 std (249 €) | 2 pilotes (99 €) + 7 std (249 €) + 2 rest (399 €) |
| **Revenu total encaissé (€)** | **198,00 €** | **1 194,00 €** | **2 739,00 €** |
| **Revenu total en FCFA** | **129 880 FCFA** | **783 213 FCFA** | **1 796 667 FCFA** |

---

## 6. Analyse de Sensibilité

### 6.1 Sensibilité de Veille-Intel au Taux de Closing et à la Date de Signature
Montant encaissé en € au 31/12/2026 pour 2 agences clientes signées :

| Prix Mensuel | Signature avant le 31/10 (3 mensualités) | Signature avant le 17/11 (2 mensualités) | Signature après le 17/11 (1 mensualité) |
| :---: | :---: | :---: | :---: |
| **349 €** | $2 \times 3 \times 349 = 2\,094\text{ €}$ | $2 \times 2 \times 349 = 1\,396\text{ €}$ | $2 \times 1 \times 349 = 698\text{ €}$ |
| **399 €** *(Tarif de base)* | $2 \times 3 \times 399 = \mathbf{2\,394\text{ €}}$ | $2 \times 2 \times 399 = \mathbf{1\,596\text{ €}}$ *(Plancher)* | $2 \times 1 \times 399 = \mathbf{798\text{ €}}$ |
| **499 €** *(Tarif standard)* | $2 \times 3 \times 499 = 2\,994\text{ €}$ | $2 \times 2 \times 499 = 1\,996\text{ €}$ | $2 \times 1 \times 499 = 998\text{ €}$ |

> **Constat financier majeur :** Signer 2 agences avant le 17 novembre garantit mécaniquement le dépassement du plancher de 1 000 000 FCFA ($1\,596\text{ €} > 1\,524,49\text{ €}$). Tout décalage de signature au-delà du 17 novembre divise le revenu encaissé par deux.
