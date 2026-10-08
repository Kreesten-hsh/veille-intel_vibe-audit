# Guide Opérationnel de Production des Livrables (Runbook)

> **Règle absolue (Garde-fous #3 et #4) :** Aucun envoi automatique de message. L'agent prépare, l'humain vérifie, valide et envoie manuellement. Aucune analyse d'une cible sans consentement écrit enregistré.

---

## 1. Procédure Pas à Pas : Veille-Intel (Abonnement Hebdomadaire)

### 1.1 Objectifs de Temps
- **Temps cible humain : Moins de 45 minutes par client et par semaine.**
- Rythme de production : Traitement le lundi matin pour livraison avant 12h00.

### 1.2 Déroulement Étape par Étape

```
[ Lundi 08h00 ] Préparation & Vérification de la Configuration
      │
      ▼
[ Lundi 08h10 ] Collecte Passive & Snapshots (uv run veille-intel fetch)
      │
      ▼
[ Lundi 08h20 ] Calcul Différentiel Local (uv run veille-intel diff)
      │
      ▼
[ Lundi 08h30 ] Structuration des Signaux (uv run veille-intel format-signals)
      │
      ▼
[ Lundi 08h45 ] Revue Humaine Éditoriale (Validation des faits + 3 actions)
      │
      ▼
[ Lundi 09h00 ] Rendu PDF Marque Blanche & Contrôle Qualité Final
      │
      ▼
[ Lundi 09h15 ] Envoi Manuel par Email à l'Agence
```

#### Étape 1 : Préparation & Configuration (Durée : 5 min)
1. Ouvrir le fichier de configuration dans `config/clients/<client_id>.yaml`.
2. Vérifier que la liste comporte au maximum 5 concurrents et des URLs publiques actives (pricing, changelog, blog, carrières).

#### Étape 2 : Collecte Passive & Snapshots (Durée : 10 min)
1. Lancer la collecte passive :
   ```bash
   uv run veille-intel fetch --client <client_id>
   ```
2. Le moteur interroge le `robots.txt` de chaque domaine, temporise 5 secondes entre chaque requête et enregistre le texte brut nettoyé dans `data/veille_intel.db`.

#### Étape 3 : Calcul Différentiel Local (Durée : 5 min)
1. Exécuter la comparaison de la semaine N par rapport à la semaine N-1 :
   ```bash
   uv run veille-intel diff --client <client_id>
   ```
2. Si un concurrent n'a subi aucune modification, le système consigne explicitement : « Aucune modification observée cette semaine ».

#### Étape 4 : Structuration des Signaux & Éditorialisation (Durée : 15 min)
1. Générer le canevas des signaux bruts :
   ```bash
   uv run veille-intel format-signals --client <client_id>
   ```
2. Ouvrir le fichier de travail généré `drafts/<client_id>_S<semaine>.md`.
3. **Intervention humaine de l'opérateur :**
   - Vérifier la pertinence des deltas extraits (ex. changement de palier tarifaire, publication d'un nouvel article clé, recrutement d'un poste stratégique).
   - Formuler pour chaque signal retenu (5 à 10 au total) :
     - « Ce qui a changé » (description factuelle brute).
     - « Interprétation » (analyse stratégique séparée du fait).
     - « 3 actions recommandées » (pistes concrètes pour l'agence ou son client).

#### Étape 5 : Rendu PDF & Expédition Manuelle (Durée : 10 min)
1. Compiler le livrable final marque blanche :
   ```bash
   uv run veille-intel render --client <client_id> --output export/<client_id>_S<semaine>.pdf
   ```
2. Si WeasyPrint n'est pas disponible sur le système, ouvrir le fichier HTML généré (`export/<client_id>_S<semaine>.html`) dans le navigateur et imprimer en PDF.
3. Exécuter la checklist pré-livraison (section 3.1 ci-dessous).
4. Joindre le PDF et envoyer l'email personnalisé manuellement au contact de l'agence.

---

## 2. Procédure Pas à Pas : Vibe-Audit (Mission Express 48 h)

### 2.1 Objectifs de Temps
- **Délai client : Rapport remis sous 48 heures ouvrées après commande.**
- **Temps cible humain : Moins de 3 heures de travail cumulé sur les 48 h.**
- **Échantillon de démonstration :** application créée par l'opérateur, volontairement vulnérable, dont il est propriétaire. Jamais l'application d'un tiers sans consentement écrit.

### 2.2 Déroulement Étape par Étape

#### Étape 1 : Sas de Consentement Obligatoire (J0 - Matin)
1. Réception de la commande et de l'accord écrit du fondateur.
2. Déposer et valider le fichier `consent/<client_id>.md` :
   - Identité du signataire (propriétaire légitime).
   - Périmètre exact : URL publique consentie, référence du dépôt ou de l'archive.
   - Période d'autorisation (date de début et date de fin).
3. **Contrôle bloquant :** Exécuter la vérification préalable :
   ```bash
   uv run vibe-audit verify-consent --client <client_id>
   ```
   *La CLI refuse tout traitement si cette étape ne renvoie pas un statut valide.*

#### Étape 2 : Ingestion et Scans Statiques Locaux (J0 - Après-midi)
1. Extraire l'archive du code source dans un répertoire de travail isolé et ignoré par git (`work/<client_id>/`).
2. Lancer la batterie d'analyses statiques locales :
   ```bash
   uv run vibe-audit scan --target work/<client_id> --url <url_publique> --consent consent/<client_id>.md
   ```
   - Détection des secrets dans le code et dans l'historique des commits (`git log -p`).
   - Analyse syntaxique des scripts de migration SQL Supabase (détection de tables sans RLS ou avec `USING (true)`).
   - Audit statique des dépendances déclarées (`package-lock.json` via `npm audit --package-lock-only`, `pip-audit`).
   - Analyse passive des en-têtes HTTP de sécurité et CORS sur l'URL publique consentie.

#### Étape 3 : Reproduction Manuelle & Qualification (J+1)
1. **Règle absolue : Zéro faux positif.**
2. L'opérateur passe en revue chaque constat brut consigné dans `data/vibe_audit.db`.
3. Reproduire manuellement chaque vulnérabilité :
   - Tester si une table Supabase répond effectivement aux requêtes avec la clé anonyme publique sans authentification.
   - Vérifier la réalité de l'exposition d'un token d'API.
4. Écarter formellement tout faux positif ou constat non prouvé.

#### Étape 4 : Rédaction des Prompts de Correction & Rapport (J+2 - Matin)
1. Générer le rapport préliminaire :
   ```bash
   uv run vibe-audit report --client <client_id> --output export/audit_<client_id>.pdf
   ```
2. Vérifier que chaque vulnérabilité documentée comprend :
   - Le niveau de gravité (Critique, Élevé, Moyen, Faible).
   - La preuve matérielle reproductible (requête curl passive ou extrait de ligne de code masqué).
   - L'impact concret en français simple compréhensible par un fondateur non technique.
   - Le **prompt prêt à copier-coller** pour Lovable, Bolt ou Cursor permettant d'appliquer le correctif immédiatement.
   - La section transparente listant les périmètres non testés.

#### Étape 5 : Livraison Manuelle & Clôture (J+2 - Après-midi)
1. Exécuter la checklist pré-livraison (section 3.2).
2. Envoyer le rapport PDF par email au fondateur avec le récapitulatif des constats majeurs.
3. Si la formule inclut la restitution (399 €) : tenir l'appel de débriefing de 30 minutes.
4. Programmer dans l'agenda un rappel à J+14 pour proposer la contre-visite gratuite de vérification des correctifs.

---

## 3. Checklists de Vérification Avant Livraison

### 3.1 Checklist Pré-Livraison : Veille-Intel
- [ ] **100 % des signaux sont sourcés :** Chaque signal contient une URL active et une date de capture vérifiable.
- [ ] **Séparation stricte faits / opinions :** Aucun fait n'est déformé ; l'interprétation stratégique est clairement identifiée comme telle.
- [ ] **Zéro marque technique :** Aucune mention de `veille-intel`, de script, d'IA ou de prestataire n'apparaît dans le document (100 % marque blanche agence).
- [ ] **Gestion de l'inactivité :** Si un concurrent n'a rien publié, la mention « Aucun changement observé » figure sans invention de signal.
- [ ] **Rendu visuel :** Document entre 3 et 6 pages, typographie soignée, absence de texte tronqué ou de saut de page incohérent.
- [ ] **Envoi manuel :** Le message est envoyé individuellement depuis le client de messagerie personnel de l'opérateur.

### 3.2 Checklist Pré-Livraison : Vibe-Audit
- [ ] **Consentement enregistré :** Le fichier `consent/<client_id>.md` est complet, signé et archivé.
- [ ] **Secrets masqués :** Aucune clé privée, token ou mot de passe réel n'apparaît en clair dans le rapport (masquage systématique `sk-****`).
- [ ] **Preuves reproductibles :** 100 % des constats présentés ont été testés et validés manuellement par l'opérateur.
- [ ] **Prompts de remédiation validés :** Les prompts de correction fournis sont clairs, syntaxiquement corrects et adaptés à l'outil no-code du client.
- [ ] **Transparence sur les exclusions :** La section listant ce qui n'a pas été testé est présente et explicite.
- [ ] **Confidentialité post-audit :** Rappel de suppression définitive des copies locales de code sous 30 jours calendaires.

---

## 4. Procédures en Cas d'Échec ou d'Incident

### Incident 1 : Page cible inaccessible ou erreur HTTP (403, 404, 429) lors de la veille
- **Action immédiate :** Ne jamais tenter de contourner la protection, ne pas changer d'IP, ne pas forcer la requête.
- **Traitement :** Consigner l'indisponibilité dans le rapport hebdomadaire :
  > *« Note : La page [URL] était temporairement inaccessible (code HTTP [XXX]) lors de notre capture du [Date]. Aucune modification n'a pu être relevée cette semaine sur cette source. »*
- L'opérateur vérifie manuellement la semaine suivante si la page a changé d'adresse.

### Incident 2 : Découverte d'une fuite critique de données réelles d'utilisateurs (Vibe-Audit)
- **Scénario :** Lors de l'inspection de la configuration Supabase consentie, l'opérateur constate que la base expose des données sensibles en clair (emails, mots de passe, données financières).
- **Règle absolue d'arrêt d'urgence :**
  1. **Arrêt immédiat :** Interruption sur-le-champ de l'audit.
  2. **Zéro copie :** Ne copier, ne télécharger et ne stocker aucune donnée personnelle client.
  3. **Notification confidentielle :** Avertir le fondateur en privé et en urgence (email ou appel direct) pour lui permettre de couper la table ou d'activer immédiatement la RLS.
  4. Reprise de l'audit uniquement après sécurisation de l'incident.

### Incident 3 : Dépendances graphiques WeasyPrint manquantes
- **Symptôme :** Erreur lors de la compilation PDF automatique (`cannot load library 'pango' / 'cairo'`).
- **Procédure de repli :**
  1. Le moteur génère automatiquement le fichier HTML autonome dans `export/`.
  2. Ouvrir le fichier HTML dans le navigateur (Chrome / Firefox).
  3. Sélectionner **Imprimer** $\rightarrow$ Destination : **Enregistrer au format PDF** $\rightarrow$ Activer l'option « Graphiques d'arrière-plan ».
  4. Vérifier le rendu et délivrer le PDF ainsi produit.

### Incident 4 : Désaccord du client ou contestation d'un constat (Vibe-Audit)
- **Action :** Réexaminer la preuve enregistrée dans `data/vibe_audit.db`. Si le client démontre qu'une protection additionnelle neutralise la faille, retirer immédiatement le constat du rapport final avec mention explicite de la vérification contradictoire.
