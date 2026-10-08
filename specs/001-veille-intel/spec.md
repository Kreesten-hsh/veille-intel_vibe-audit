# Spécification Fonctionnelle : Moteur de Veille Concurrentielle Passive (veille-intel)

**Feature Branch** : `001-veille-intel`  
**Date de création** : 2026-10-08  
**Statut** : Validé  
**Entrée** : docs/01-PRD.md, docs/04-ARCHITECTURE.md, docs/05-STRATEGIE-DE-TEST.md  

---

## Scénarios Utilisateur & Tests d'Acceptation

### User Story 1 - Surveillance Passive & Capture d'Instantanés (Priorité : P1 - MVP)

En tant qu'opérateur (Kreesten), je veux collecter de manière passive et respectueuse le contenu public des pages cibles (sites concurrents, flux RSS, annonces publiques) d'un client afin de conserver un historique horodaté des instantanés.

**Pourquoi cette priorité** : Sans acquisition de données fiable et conforme (robots.txt, respect de la bande passante), aucune analyse n'est possible.

**Test Indépendant** : Peut être testé isolément en simulant des réponses HTTP locales (fixtures mockées) et en vérifiant la persistance dans la base SQLite locale.

**Scénarios d'Acceptation** :
1. **Étant donné** une URL cible autorisée par son `robots.txt`, **Quand** le collecteur s'exécute, **Alors** la page est récupérée avec un délai minimal de 5s entre requêtes et l'instantané HTML/texte est enregistré avec son hash SHA-256.
2. **Étant donné** une URL cible dont le `robots.txt` interdit l'accès au User-Agent ou une ressource inaccessible (erreur 404, 500, timeout), **Quand** le collecteur s'exécute, **Alors** l'URL est ignorée ou marquée en échec sans bloquer le reste de la collecte, et l'événement est consigné dans les logs.

---

### User Story 2 - Détection Déterministe de Changements & Diff Structuré (Priorité : P2)

En tant qu'opérateur, je veux comparer automatiquement le dernier instantané d'une page avec l'instantané précédent afin d'identifier les ajouts, suppressions et modifications significatives (tarifs, offres, nouvelles fonctionnalités, articles de blog).

**Pourquoi cette priorité** : Élimine le bruit (scripts, horodatages dynamiques, balises publicitaires) pour ne retenir que les signaux d'affaires à forte valeur ajoutée.

**Test Indépendant** : Peut être testé en fournissant deux versions HTML d'une page de tarification et en vérifiant que le rapport de diff extrait exactement la variation de prix ou de libellé sans faux positif.

**Scénarios d'Acceptation** :
1. **Étant donné** deux instantanés successifs d'une même page avec des modifications textuelles, **Quand** le module de diff s'exécute, **Alors** il extrait un résumé structuré des sections modifiées et ignore les métadonnées volatiles (nonces de script, timestamps).
2. **Étant donné** deux instantanés strictement identiques ou sans changement substantiel, **Quand** le module s'exécute, **Alors** il marque le statut "aucun changement significatif" sans générer de faux signal.

---

### User Story 3 - Génération du Livrable Hebdomadaire en Marque Blanche (Priorité : P3)

En tant qu'opérateur, je veux compiler les changements détectés de la semaine dans un rapport HTML autonome propre et stylisé aux couleurs de l'agence cliente (marque blanche), prêt à être exporté ou imprimé en PDF en moins de 45 minutes.

**Pourquoi cette priorité** : C'est le produit fini livré au client justifiant l'abonnement mensuel récurrent (399 € - 499 €/mois).

**Test Indépendant** : Peut être testé en injectant une liste de diffs synthétiques et en vérifiant que le fichier HTML produit contient l'en-tête de l'agence cliente, la table des matières, les signaux clés, et ne contient aucune fuite technique interne.

**Scénarios d'Acceptation** :
1. **Étant donné** un jeu de signaux validés pour une agence cliente, **Quand** le moteur de rendu s'exécute avec le gabarit Jinja2, **Alors** un document HTML autonome valide (styles CSS intégrés, responsive, prêt pour impression PDF) est généré dans `output/reports/<client>_<date>.html`.

---

## Cas Limites (Edge Cases)

- **Page inaccessible / Timeout réseau** : Le collecteur effectue au maximum 2 tentatives avec backoff exponentiel (1s, 2s). En cas d'échec persistant, la cible est marquée `INDISPONIBLE` et le rapport hebdomadaire le mentionne clairement.
- **Modification massive de structure (refonte de site)** : Si le diff dépasse 80 % du contenu, le système génère une alerte "Refonte majeure détectée" au lieu de lister ligne par ligne l'ensemble du DOM.
- **Flux RSS absent ou corrompu** : Repli automatique sur l'extraction de liens et titres depuis le flux HTML de la page d'actualités/blog.
- **Contenu textuel vide après nettoyage** : L'alerte "Contenu vide" est consignée et aucune notification fallacieuse n'est injectée dans le rapport.

---

## Exigences Fonctionnelles (FR)

- **FR-001** : Le système DOIT charger la configuration des cibles (URLs, sélecteurs CSS optionnels, périodicité, métadonnées de l'agence cliente) depuis un fichier YAML ou JSON local.
- **FR-002** : Le collecteur DOIT vérifier l'autorisation du fichier `robots.txt` de chaque domaine cible avant toute requête.
- **FR-003** : Le collecteur DOIT respecter un espacement strict d'au moins 5 secondes entre deux requêtes vers un même domaine et utiliser un User-Agent identificatoire honnête.
- **FR-004** : Le système DOIT persister les instantanés (URL, horodatage UTC, contenu épuré, hash SHA-256) dans une base SQLite locale (`data/veille.db`).
- **FR-005** : Le moteur de diff DOIT comparer l'instantané courant avec le dernier instantané valide pour déterminer le delta textuel et structurel.
- **FR-006** : Le système DOIT classifier les deltas selon 4 catégories déterministes : `Tarification & Offre`, `Produit & Fonctionnalité`, `Communication & Contenu`, `Organisation & Recrutement`.
- **FR-007** : Le générateur de rapport DOIT utiliser un gabarit Jinja2 autonome intégrant la personnalisation en marque blanche (nom de l'agence, logo vectoriel, palette de couleurs).
- **FR-008** : Le système DOIT fonctionner à 100 % hors-ligne lors des tests unitaires et d'intégration grâce à des fixtures pré-enregistrées.
