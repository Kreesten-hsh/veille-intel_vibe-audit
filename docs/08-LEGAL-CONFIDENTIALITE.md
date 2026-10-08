# Cadre Juridique, Confidentialité des Données & Conformité Réglementaire

> **Avertissement :** Ce document fixe les obligations déontologiques, techniques et juridiques du projet. Tout élément non confirmé par une source officielle ou en attente d'une validation par un professionnel du droit est formellement marqué **[À VÉRIFIER]**.

---

## 1. Protocole de Consentement Écrit Obligatoire (Vibe-Audit)

L'audit de sécurité d'un système informatique tiers sans accord exprès constitue une infraction pénale (articles 323-1 à 323-3-1 du Code pénal français réprimant l'atteinte aux systèmes de traitement automatisé de données).

### 1.1 Conditions de Validité du Consentement
- **Aucune analyse n'est exécutée** tant que le fichier de consentement écrit [docs/CONSENTEMENT.md](file:///home/hasashi/Bureau/veille-intel_vibe-audit/docs/CONSENTEMENT.md) n'a pas été complété et signé par le client, puis archivé sous `consent/<client_id>.md`.
- Le consentement doit stipuler obligatoirement :
  1. **L'identité du signataire :** Nom, qualité, et déclaration sur l'honneur attestant être le propriétaire légitime ou le représentant habilité de l'application et de son code source.
  2. **Le périmètre technique exhaustif :** URL publique de production ou de recette autorisée, URL du dépôt git ou empreinte de l'archive ZIP autorisée.
  3. **La fenêtre temporelle d'intervention :** Date exacte de début et date de fin d'autorisation des contrôles.
  4. **La nature strictement passive des tests :** Accord limité à l'analyse statique du code et à des requêtes HTTP passives de vérification de configuration. Interdiction absolue d'attaques par force brute, d'injections SQL destructives ou d'extraction de données réelles d'utilisateurs.

### 1.2 Procédure d'Arrêt d'Urgence en Cas de Découverte de Données Réelles
Si lors d'une vérification de politique d'accès Supabase / PostgreSQL, l'opérateur constate que la table expose publiquement des données personnelles réelles (PII) d'utilisateurs en production :
1. **Arrêt immédiat** de toute vérification technique.
2. **Interdiction absolue** de copier, télécharger, archiver ou exploiter les données visualisées.
3. **Alerte immédiate et confidentielle** transmise au fondateur du projet par canal direct prioritaire.

---

## 2. Prospection Électronique B2B & Droit d'Opposition (RGPD)

La prospection commerciale directe par email entre professionnels en France est régie par l'article L. 34-5 du Code des postes et des communications électroniques et par le Règlement Général sur la Protection des Données (RGPD - Règlement UE 2016/679).

### 2.1 Base Légale : L'Intérêt Légitime
- En matière B2B, le consentement préalable (opt-in) n'est pas requis pour l'envoi d'emails professionnels, sous réserve du respect cumulatif de trois conditions :
  1. Le destinataire est sollicité au titre de ses fonctions professionnelles (ex. gérant d'agence marketing pour Veille-Intel, créateur d'app pour Vibe-Audit).
  2. L'objet du message est en lien direct avec son activité professionnelle.
  3. L'adresse email a été collectée sur une source publique accessible à tous (mentions légales, page de contact du site de l'agence, profil professionnel public).

### 2.2 Exercice Effectif du Droit d'Opposition
- **Information obligatoire :** Chaque email envoyé comporte une mention informant le prospect de son droit de s'opposer sans frais ni justification à toute future sollicitation.
- **Mécanisme simplifié :** Possibilité de s'opposer par simple réponse au message (mot « STOP » ou « OPPOSITION »).
- **Registre d'opposition :** Tout refus est consigné dans [docs/PROSPECTS.csv](file:///home/hasashi/Bureau/veille-intel_vibe-audit/docs/PROSPECTS.csv) (`opposition = oui`). Aucune relance ni nouveau contact ne doit jamais être adressé à une adresse inscrite sur ce registre.

---

## 3. Confidentialité & Protection des Données Clients

Conformément à la décision d'architecture ADR-02 :
1. **Traitement 100 % local et déterministe :** Aucun code source client, aucune politique de base de données, ni aucun nom d'agence/client n'est transmis à un service tiers, une API LLM cloud ou une plateforme distante.
2. **Étanchéité des dépôts Git :** Le fichier `.gitignore` exclut formellement les répertoires `work/` (copies de code client), `consent/` (pièces signées), `data/` (bases SQLite locales) et `.env`.
3. **Masquage systématique des secrets :** Toute clé privée ou token découvert lors d'un scan est tronqué dans les rapports et journaux (ex. `sk-proj-****`).
4. **Purge et destruction à 30 jours :** Les copies locales de code et les archives d'audit sont irrémédiablement supprimées du disque local 30 jours calendaires après remise du rapport final.

---

## 4. Points de Vigilance Juridiques et Fiscaux

### 4.1 Points à Vérifier auprès de la CNIL
1. **Statut au sens du RGPD (Sous-traitant vs Responsable de traitement) :**
   - Pour Veille-Intel : l'opérateur est responsable de traitement des données de veille publique collectées.
   - Pour Vibe-Audit : si le code audité contient par mégarde des extraits de bases avec des données réelles d'utilisateurs finaux, l'opérateur pourrait être qualifié de sous-traitant. Un contrat de sous-traitance de données (DPA) simplifié est-il requis pour l'audit ? **[À VÉRIFIER auprès de la CNIL]**.
2. **Durée de conservation des instantanés textuels de veille :**
   - La conservation du texte brut archivé dans SQLite pour comparaison différentielle est fixée à 1 an glissant. La conformité de cette durée vis-à-vis du droit à l'effacement de personnes mentionnées dans des articles de blog publics est **[À VÉRIFIER]**.

### 4.2 Points Fiscaux et Facturation
1. **Statut d'émission de la facture au nom personnel de Kreesten :**
   - Émission en tant que consultant indépendant basé au Bénin sans numéro de TVA français.
   - Mention légale sur facture : conformité de la dispense de TVA selon les règles internationales de territorialité des prestations de services B2B (règle preneur / assujetti de l'art. 259 B du CGI pour un client assujetti en France) **[À VÉRIFIER auprès d'un expert-comptable]**.
2. **Acceptabilité bancaire des factures par les entreprises françaises :**
   - Les agences françaises peuvent déduire en charges les factures de prestataires étrangers hors UE, sous réserve de la présence des mentions obligatoires (identité complète, date, prestation détaillée, montant, coordonnées bancaires). L'existence d'une retenue à la source spécifique sur les prestations informatiques Bénin-France est **[À VÉRIFIER dans la convention fiscale bilatérale franco-béninoise]**.
3. **Régime fiscal local au Bénin :**
   - Déclaration des revenus perçus auprès de l'administration fiscale béninoise (Identifiant Fiscal Unique - IFU, régime de la TPS ou régime réel selon volume d'affaires) **[À VÉRIFIER auprès d'un fiscaliste local]**.
