# Guide Opérationnel de l'Opérateur (Runbook)

Ce document décrit le cycle opératoire complet pour un opérateur unique, sans équipe et sans budget d'infrastructure.

---

## 1. Cycle Opérationnel : Veille-Intel (Hebdomadaire)

### Objectif de Temps
- **Moins de 45 minutes de travail humain par client chaque semaine.**

### Déroulement Pas à Pas

#### Étape 1 : Initialisation & Configuration (Lundi 08h00)
1. Vérifier la présence du fichier client dans `config/clients/<client_id>.yaml` (nom d'affichage, 5 concurrents, URLs cibles).
2. Lancer la collecte de données :
   ```bash
   uv run veille-intel fetch --client <client_id>
   ```
   - Le module interroge le `robots.txt` de chaque domaine.
   - Il applique le délai de politesse (5 secondes entre requêtes).
   - Il sauvegarde les snapshots HTML bruts dans SQLite (`data/veille_intel.db`).

#### Étape 2 : Calcul du Différentiel N vs N-1
1. Exécuter le module de comparaison :
   ```bash
   uv run veille-intel diff --client <client_id>
   ```
2. Si aucun changement n'est détecté sur un concurrent : l'information est notée comme « Aucune modification observée » (zéro hallucination de faux signal).

#### Étape 3 : Structuration des Signaux & Rédaction (Logique locale & Révision humaine)
1. Lancer la structuration des deltas textuels :
   ```bash
   uv run veille-intel format-signals --client <client_id>
   ```
   - Le moteur isole les sections modifiées (tarifs, titres de blog, recrutements) et génère le canevas horodaté.
   - Traitement 100 % local et déterministe (zéro API externe, zéro clé). L'opérateur finalise les recommandations actionnables.

#### Étape 4 : Validation Humaine Obligatoire (Revue de 15 minutes)
1. Ouvrir le brouillon généré.
2. Vérifier que chaque signal pointe vers une URL active et une date exacte.
3. Supprimer tout signal douteux ou non étayé par une preuve matérielle.
4. Ajuster les recommandations selon le contexte métier de l'agence.

#### Étape 5 : Export & Livraison Manuelle
1. Générer le PDF final marque blanche :
   ```bash
   uv run veille-intel render --client <client_id> --output export/<client_id>_S<semaine>.pdf
   ```
2. Ouvrir le PDF, inspecter le rendu visuel (3 à 6 pages, zéro marque d'outil).
3. Envoyer manuellement par email au contact de l'agence depuis son client de messagerie.

---

## 2. Cycle Opérationnel : Vibe-Audit (Mission 48h)

### Déroulement Pas à Pas

#### Étape 1 : Sas de Consentement Préalable (J0)
1. Vérifier la réception du consentement écrit signé par le propriétaire de l'application.
2. Créer le fichier `consent/<client_id>.md` :
   - Nom et contact du signataire.
   - Dépôt de code autorisé / URL publique consentie.
   - Date de début et date de fin d'autorisation.
3. **Condition bloquante** : La CLI refusera de démarrer si ce fichier est absent.

#### Étape 2 : Ingestion et Analyses Statiques Locales (J0 - J+1)
1. Cloner ou décompresser l'archive du code dans un répertoire de travail temporaire ignoré par git (`work/<client_id>/`).
2. Exécuter la batterie de contrôles locaux :
   ```bash
   uv run vibe-audit scan --target work/<client_id> --url <url_publique> --consent consent/<client_id>.md
   ```
   - Détection locale des secrets et clés d'API (fichiers sources et historique git).
   - Analyse des politiques RLS Supabase (requêtes SQL / migrations).
   - Audit des dépendances vulnérables (`npm audit` ou `pip-audit`).
   - Analyse passive des en-têtes HTTP et TLS sur l'URL publique.

#### Étape 3 : Validation et Reproduction Manuelle (J+1)
1. **Règle absolue : Aucun faux positif.**
2. L'opérateur prend chaque constat détecté et le reproduit manuellement (ex : vérifier si la table Supabase répond effectivement sans token d'authentification).
3. Si une vulnérabilité expose de vraies données clients sensibles :
   - Arrêt immédiat de l'audit.
   - Notification d'urgence au client en privé sans enregistrer la donnée.

#### Étape 4 : Rédaction des Prompts de Fixation & Rapport PDF (J+2)
1. Générer le rapport préliminaire :
   ```bash
   uv run vibe-audit report --client <client_id> --output export/audit_<client_id>.pdf
   ```
2. S'assurer que chaque constat comprend :
   - Preuve reproductible et niveau de criticité.
   - Explication de l'impact métier en français simple.
   - Prompt prêt à coller pour Lovable, Bolt ou Cursor permettant d'appliquer le correctif.
   - Mention expresse des éléments non testés.

#### Étape 5 : Livraison et Re-contrôle J+14
1. Envoi manuel du PDF au fondateur par email.
2. Si formule avec restitution (399 €) : tenue de la visio de débriefing de 45 minutes.
3. Programmer dans le calendrier un rappel à J+14 pour proposer le re-contrôle gratuit des correctifs.

---

## 3. Gestion des Incidents & Cas Dégradés

- **Page inaccessible / Erreur 403 / 429 lors de la veille** :
  - Ne jamais forcer la requête ni tenter de contournement.
  - Consigner dans le rapport : « Source temporairement indisponible lors de la capture du [Date] ».
- **Absence de dépendances graphiques WeasyPrint** :
  - Le système exporte directement le rapport au format HTML/CSS standalone. L'opérateur ouvre le fichier dans son navigateur et sélectionne « Imprimer en PDF » en 2 clics.
