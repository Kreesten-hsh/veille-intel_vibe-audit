# Constitution du Projet Veille-Intel & Vibe-Audit

<!-- Version: 1.0.0 | Ratifiée: 2026-10-08 | Règle absolue du projet -->

## Principes Fondamentaux (Non Négociables)

### I. Zéro Dépense & Zéro Dette Financière (Capital Zéro)
- Aucun service payant, aucune clé d'API payante, aucun essai gratuit exigeant une carte bancaire.
- Tout service LLM cloud tiers ou API externe est formellement **ÉCARTÉ** du runtime applicatif. Le moteur de traitement repose à 100 % sur du code Python local déterministe (expressions régulières, diffs structurés, parsers HTML/RSS, heuristiques).
- Facturation et encaissement : virement bancaire pur (Moneco SEPA / Ecobank Bénin). Zéro intégration Stripe, PayPal, Payoneer ou Wise.

### II. Légalité, Éthique Passive & Consentement Enregistré
- **Vibe-Audit** : Aucune analyse de sécurité d'une cible sans consentement écrit explicite et horodaté enregistré dans `consent/<client>.md`.
- **Veille-Intel** : Surveillance passive exclusive. Respect strict des `robots.txt`, délai minimal de 5 secondes entre requêtes vers un même domaine, en-tête `User-Agent` transparent et honnête, pas de contournement de paywall, de login ou de CAPTCHA.

### III. Local-First & Zéro Fuite de Données
- Aucun secret, token ou donnée client dans Git. `.env` et répertoires de données clients sont strictement ignorés (`.gitignore`).
- Les suites de tests s'exécutent à 100 % hors-ligne avec des fixtures synthétiques anonymisées.

### IV. Zéro Hallucination & Rigueur Factuelle
- Aucun chiffre, aucune source, aucune vulnérabilité inventés.
- Distinction stricte entre fait avéré et interprétation/recommandation. Tout élément non confirmé par un fait observable est explicitement marqué `[NON VÉRIFIÉ]`.

### V. Développement Piloté par les Tests (Test-First) & Simplicité
- Tests unitaires et d'intégration écrits avant ou conjointement avec chaque lot fonctionnel.
- Pas de sur-architecture, pas d'abstractions prématurées. Modules clairs, typés et documentés.

### VI. Incrémentalité par Lot & Validation Humaine
- Pour toute implémentation via Spec-Kit, **un seul lot à la fois avec ses tests** est préparé et soumis à l'approbation explicite de l'opérateur avant de passer au lot suivant.
- L'agent prépare, l'humain valide et expédie. Aucun envoi automatisé d'emails ou de rapports vers l'extérieur.

## Stack & Limites Techniques

- **Langage & Environnement** : Python 3.12, gestionnaire `uv`.
- **Bibliothèques Autorisées** : `httpx` (client HTTP passif), `beautifulsoup4` / `selectolax` (parsing HTML), `jinja2` (génération de rapports), `sqlite3` (persistance locale légère), `pytest` (tests).
- **Format de Sortie** : Rapports HTML autonomes imprimables en PDF (fallback natif zéro dépendance binaire complexe).

## Gouvernance

Cette constitution prévaut sur toute directive d'implémentation ou commodité technique. Toute déviation nécessite un accord explicite de l'opérateur.

**Version**: 1.0.0 | **Ratifiée**: 2026-10-08 | **Dernière révision**: 2026-10-08
