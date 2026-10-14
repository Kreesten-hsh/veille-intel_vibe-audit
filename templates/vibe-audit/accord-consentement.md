---
reference: "VA-CONSENT-YYYYMMDD-XXXX"
client_nom: "[NOM ET PRÉNOM DU COMMANDITAIRE]"
client_qualite: "[FONDATEUR / CEO / CTO / MANDATAIRE HABILITÉ]"
societe_projet: "[NOM DU PROJET / SOCIÉTÉ]"
client_email: "[EMAIL PROFESSIONNEL DU COMMANDITAIRE]"
auditeur_nom: "Kreesten Agboton"
auditeur_qualite: "Consultant indépendant en sécurité des systèmes d'information"
url_cible: "[https://app.monprojet.com]"
repo_ou_archive: "[URL DÉPÔT GIT OU NOM ARCHIVE CODE]"
date_debut: "[YYYY-MM-DDTHH:MM:SSZ]"
date_expiration: "[YYYY-MM-DDTHH:MM:SSZ]"
recheck_expiration: "[YYYY-MM-DDTHH:MM:SSZ]"
statut: "VALIDE"
---

# Mandat d'Évaluation Technique Passive & Accord Bilatéral de Confidentialité (NDA)
**Vibe-Audit · Audit de Sécurité Express pour Applications Web & No-Code**

---

### Préambule Légal
Conformément aux articles 323-1 à 323-3-1 du Code pénal français réprimant l'atteinte aux systèmes de traitement automatisé de données, et aux dispositions du Règlement Général sur la Protection des Données (RGPD - Règlement UE 2016/679), **aucune opération de diagnostic ou de contrôle technique ne peut être engagée sans le consentement exprès, préalable et enregistré du propriétaire légitime des actifs visés**.

Le présent contrat formalise le mandat d'intervention passif et l'accord réciproque de confidentialité liant le Commanditaire et le Prestataire.

---

### 1. Parties Prenantes

#### Le Commanditaire (Client)
- **Nom et Prénom :** [NOM ET PRÉNOM DU COMMANDITAIRE]
- **Qualité / Titre :** [Fondateur / CEO / CTO / Représentant légal habilité]
- **Nom du Projet / Société :** [NOM DE L'APPLICATION OU STRUCTURE COMMERCIALE]
- **Email de contact :** [EMAIL DU COMMANDITAIRE]
- **Attestation de propriété :** Le Commanditaire déclare et atteste sur l'honneur disposer des droits de propriété intellectuelle légitimes ou d'un mandat de gestion exprès sur le code source, les bases de données et les domaines désignés à l'Article 2.

#### Le Prestataire (Auditeur)
- **Nom et Prénom :** Kreesten Agboton
- **Qualité :** Consultant indépendant en sécurité des systèmes d'information
- **Localisation :** Abomey-Calavi, Bénin
- **Contact professionnel :** [EMAIL PROFESSIONNEL AUDITEUR]

---

### 2. Mandat d'Évaluation Passif & Périmètre Autorisé

Le Commanditaire donne formellement mandat au Prestataire pour réaliser un diagnostic de sécurité technique express (**Vibe-Audit**), strictement circonscrit au périmètre suivant :

| Composant | Élément Autorisé | Nature de l'Inspection |
|---|---|---|
| **URL Publique / Staging** | `[https://app.monprojet.com]` | Requêtes passives d'en-têtes HTTP (CSP, CORS, HSTS), vérification de surface sans injection. |
| **Code Source** | Dépôt Git en lecture seule ou archive ZIP | Analyse statique locale des dépendances (lockfiles) et des configurations front-end (`.env`, bundles). |
| **Bases de Données & API** | Fichiers SQL de migration / schémas Supabase | Examen syntaxique des politiques Row Level Security (RLS) et des contrôles d'accès objets (BOLA/IDOR). |

#### Exclusions Strictes du Périmètre
- **Infrastructures de paiement tierces :** Aucun test direct sur les infrastructures de Stripe, PayPal ou tout autre processeur bancaire.
- **Serveurs et tiers non mandatés :** Tout service cloud, sous-domaine ou fournisseur non expressément listé ci-dessus est formellement exclu.
- **Interdiction absolue d'attaques actives :** Sont strictement proscrits : toute attaque par force brute, tout déni de service (DoS/DDoS), toute altération, suppression ou écriture de données, ainsi que toute exploitation agressive de vulnérabilité.

---

### 3. Accord de Confidentialité Réciproque (NDA) & Traitement des Données

1. **Secret Professionnel & Non-Divulgation :**
   - Le Prestataire s'engage à traiter le code source, les architectures, les identifiants techniques et les vulnérabilités découvertes comme des **Informations Strictement Confidentielles**.
   - Aucune faille, preuve de concept ou mention relative au Commanditaire ne sera publiée, divulguée à un tiers ou exploitée commercialement.

2. **Traitement Local & Protection contre l'Entraînement d'IA :**
   - L'ensemble des analyses statiques et vérifications techniques est exécuté sur un poste de travail local sécurisé.
   - **Interdiction d'entraînement :** Le Prestataire garantit que le code source du Client et les données d'audit ne sont jamais soumis à des modèles publics d'intelligence artificielle ni utilisés pour l'entraînement d'algorithmes tiers.

3. **Procédure d'Arrêt d'Urgence en cas de Données Personnelles (PII) :**
   - Si, au cours de la vérification passive des politiques d'accès (RLS), des données personnelles réelles d'utilisateurs finaux apparaissent exposées :
     1. L'analyse est **interrompue immédiatement** ;
     2. **Aucune donnée personnelle n'est copiée**, téléchargée ou conservée ;
     3. Le Commanditaire est notifié en priorité et en privé dans les 2 heures avec le mode de correction immédiat.

4. **Destruction Certifiée des Données Post-Audit :**
   - Toutes les copies locales du code source, exports SQL et fichiers temporaires sont **définitivement détruits au plus tard 30 jours calendaires** après la remise du rapport final (ou immédiatement sur simple demande écrite du Client).

---

### 4. Modalités de Re-Contrôle Gratuit à J+14

Dans le cadre de l'offre Vibe-Audit, le Commanditaire bénéficie d'une **ré-évaluation passive gratuite incluse** dans un délai de 14 jours calendaires à compter de la livraison du rapport initial :

1. **Application des correctifs :** Le Commanditaire applique les prompts de remédiation et correctifs recommandés dans son outil (Lovable, Bolt, Cursor ou Supabase).
2. **Notification de re-check :** Le Commanditaire notifie le Prestataire par écrit (email ou message) en indiquant la nouvelle URL de staging ou le commit de correction.
3. **Vérification sous 24h ouvrées :** Le Prestataire exécute un re-contrôle passif ciblé sur les points corrigés et émet un avis de vérification actualisé sans frais supplémentaires.

---

### 5. Durée de Validité & Caducité

- **Début d'autorisation :** `[DATE ET HEURE UTC]`
- **Fin de la fenêtre d'audit initial :** `[DATE ET HEURE UTC (48h ouvrées maximum)]`
- **Fenêtre de re-contrôle J+14 :** Valable jusqu'à `[DATE INITIALE + 14 JOURS]`
- Au-delà de ces échéances, toute autorisation d'accès technique devient caduque de plein droit.

---

### 6. Engagement & Signature des Parties

Les parties déclarent avoir pris connaissance de l'ensemble des clauses, limitations techniques et obligations déontologiques stipulées dans le présent document.

**Cases d'engagement du Commanditaire (à cocher obligatoirement) :**
- [ ] J'atteste être le propriétaire légitime ou le représentant dûment habilité des actifs techniques audités.
- [ ] J'autorise expressément le diagnostic passif et non destructif dans les limites du périmètre défini à l'Article 2.
- [ ] J'approuve les clauses de confidentialité bilatérale (NDA) et le protocole de re-contrôle à J+14.

Fait à : `[VILLE, PAYS]`  
Le : `[DATE DU JOUR]`  

| Pour le Commanditaire (Client) | Pour le Prestataire (Auditeur) |
|---|---|
| **Nom :** [NOM DU SIGNATAIRE] | **Nom :** Kreesten Agboton |
| **Mention :** *« Bon pour mandat d'évaluation passif et accord NDA »* | **Mention :** *« Bon pour engagement de confidentialité et mandat d'audit passif »* |
| **Signature :** <br><br>_______________________________ | **Signature :** <br><br>_______________________________ |

*(Alternative numérique acceptée : accord écrit transmis par email professionnel avec la mention expresse « Bon pour mandat Vibe-Audit et accord NDA selon référence VA-CONSENT-XXXX »)*
