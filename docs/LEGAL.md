# Cadre Légal, Réglementaire et Conformité RGPD

> **Avertissement :** Ce document résume les principes de conformité appliqués au projet. Les éléments portant la mention **[À VÉRIFIER]** doivent faire l'objet d'une validation auprès d'un conseil juridique qualifié ou d'une consultation de la doctrine de la CNIL avant le premier encaissement commercial.

---

## 1. Protocole de Consentement Obligatoire (Vibe-Audit)

Conformément à l'article 323-1 et suivants du Code pénal français réprimant l'accès frauduleux à un système de traitement automatisé de données, **aucun audit n'est lancé sans consentement préalable explicite**.

### Modalités
- Un fichier `consent/<client>.md` doit exister physiquement dans le dépôt avant toute exécution de la CLI `vibe-audit`.
- Le fichier doit stipuler obligatoirement :
  - **Identité du signataire** et sa qualité de propriétaire légitime ou de représentant habilité de l'application.
  - **Périmètre strict autorisé** : Nom du dépôt, URL exacte de l'application, date de début et date de fin de la mission.
  - **Nature des tests autorisés** : Analyse statique de code et requêtes HTTP passives uniquement.
  - **Clause de confidentialité et destruction des données** : Engagement de suppression totale des copies locales de code et des données d'audit 30 jours après remise du rapport.
- **Règle d'arrêt d'urgence** : Si lors de l'analyse, l'opérateur découvre une fuite active de données à caractère personnel réelles, l'analyse s'arrête immédiatement. Aucune donnée n'est copiée ni conservée, et le client est averti sans délai via canal sécurisé.

---

## 2. Scraping Éthique et Sources Publiques (Veille-Intel)

La collecte d'informations pour la veille concurrentielle est encadrée par le respect de la loyauté des extractions et du droit de la propriété intellectuelle :

- **Sources publiques uniquement** : Aucune tentative de contournement d'accès restreint (pas de login, pas de création de faux comptes, pas de session utilisateur contournée).
- **Interdiction de contournement anti-bot** : Aucun contournement de CAPTCHA, Cloudflare Turnstile ou solutions équivalentes. Si une page bloque la requête, l'opérateur note l'indisponibilité de la source sans forcer l'accès.
- **Respect du fichier `robots.txt`** : Les directives `Disallow` sont vérifiées avant extraction.
- **Politesse et limitation de charge** :
  - Temporisation minimale obligatoire : au maximum **1 requête toutes les 5 secondes par domaine cible**.
  - En-tête `User-Agent` honnête et identifiable, indiquant explicitement la finalité de veille sans se faire passer pour un navigateur piégé.
- **Droit sui generis des bases de données (art. L. 342-1 du CPI)** : L'extraction se limite à des signaux qualitatifs ponctuels (prix unitaire, annonce d'article, offre d'emploi) sans extraction substantielle ou systématique de catalogues complets. **[À VÉRIFIER auprès d'un juriste spécialisé en propriété intellectuelle]**.

---

## 3. Prospection Commerciale B2B et RGPD

L'envoi de messages de prospection à destination de professionnels en France est encadré par l'article L. 34-5 du Code des postes et des communications électroniques et par le RGPD (Règlement UE 2016/679) :

### Base Légale : L'Intérêt Légitime
- La prospection électronique directe B2B par email ne nécessite pas un consentement préalable (opt-in) dès lors que :
  1. Le message est adressé à une personne physique au titre de son activité professionnelle (ex : directeur d'agence, fondateur de startup).
  2. L'objet de la sollicitation est en rapport direct avec la profession de la personne sollicitée (veille stratégique pour une agence, sécurité logicielle pour un fondateur).
  3. L'adresse email a été collectée loyalement sur une source publique (site internet institutionnel, registre public, mentions légales).

### Droit d'Opposition et Transparence
- **Information claire** : Chaque message de prospection indique qui contacte et la finalité de la démarche.
- **Lien d'opposition explicite** : Tout message comporte une mention informant le destinataire qu'il peut s'opposer sans motif à tout contact futur par simple réponse (« STOP » ou « OPPOSITION »).
- **Tenue du registre d'opposition** : Le fichier [PROSPECTS.csv](PROSPECTS.csv) enregistre immédiatement l'opposition (`opposition = oui`). Aucune relance ni nouveau message ne doit être envoyé à un contact opposé.

---

## 4. Points de Vigilance à Vérifier auprès de la CNIL ou d'un Avocat

1. **Rôle au sens du RGPD (Sous-traitant vs Responsable de traitement)** :
   - Pour la veille : l'opérateur agit en responsable de traitement de ses données de veille.
   - Pour l'audit : si le code ou les schémas contiennent par mégarde des échantillons de données personnelles d'utilisateurs finaux, un contrat de sous-traitance de données (DPA) peut être requis. **[À VÉRIFIER]**.
2. **Durée de conservation des journaux et des instantanés de veille** :
   - Fixer formellement la durée de purge des instantanés HTML archivés (recommandation : 1 an glissant maximum). **[À VÉRIFIER auprès de la CNIL]**.
3. **Statut d'immatriculation et facturation en micro-entreprise** :
   - Vérifier le code APE applicable (ex : 6202A Conseil en systèmes et logiciels informatiques ou 6311Z Traitement de données).
   - Seuil de franchise de TVA en prestation de services (art. 293 B du CGI). **[À VÉRIFIER avec un expert-comptable]**.
