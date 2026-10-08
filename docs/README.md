# Projet Unifié : Veille-Intel & Vibe-Audit

Ce dépôt héberge deux outils opérationnels développés en Python pour un opérateur indépendant, sous contrainte stricte de zéro dépense et conformité légale totale.

---

## Vue d'Ensemble des Deux Piliers

| Pilier | Offre & Mission | Cible | Modèle Technique |
| :--- | :--- | :--- | :--- |
| **Veille-Intel** | Veille concurrentielle hebdomadaire livrée en PDF marque blanche | Agences marketing françaises | Python 3.11+, CLI `uv`, SQLite, httpx, Jinja2 / WeasyPrint (ou HTML imprimable), moteur déterministe local |
| **Vibe-Audit** | Audit de sécurité express (48h) d'applications créées avec IA (Lovable, Bolt, Cursor) | Fondateurs non techniques francophones | Python 3.11+, CLI `uv`, SQLite, analyses statiques locales (secrets, RLS SQL, npm/pip audit), rapport PDF |

---

## Garde-fous et Principes Directeurs
Conformément à `.agents/rules/guardrails.md` :
1. **Zéro dépense** : Aucun service tiers payant, aucun essai exigeant une carte bancaire.
2. **Légalité stricte** : Consentement écrit obligatoire pour tout audit (`consent/<client>.md`) ; scraping passif de sources publiques uniquement pour la veille.
3. **Humain dans la boucle** : Jamais d'envoi automatique ; chaque rapport est revu et validé manuellement.
4. **Facturation exclusive par virement bancaire** : Aucune passerelle Stripe/PayPal/Wise.

---

## Organisation de la Documentation (`docs/`)

- [OFFRE.md](OFFRE.md) : Description détaillée des propositions de valeur et livrables.
- [TARIFS.md](TARIFS.md) : Grilles tarifaires et conditions financières.
- [FACTURE-TEMPLATE.md](FACTURE-TEMPLATE.md) : Modèle de facturation par virement conforme.
- [PROSPECTS.csv](PROSPECTS.csv) : Fichier de suivi de la prospection manuelle B2B.
- [SCRIPTS.md](SCRIPTS.md) : Messages de prise de contact, relance et argumentaires comparatifs face aux IA gratuites.
- [LEGAL.md](LEGAL.md) : Cadre juridique (RGPD, droit d'opposition, scraping, consentement écrit).
- [RUNBOOK.md](RUNBOOK.md) : Procédure pas à pas d'exécution des missions par l'opérateur.
- [GATES.md](GATES.md) : Points d'arrêt et métriques de validation commerciale (24 oct. et 10 nov.).

---

## Utilisation

1. Copier le modèle : `cp data/targets.example.yaml data/targets.yaml`.
2. Configurer les URLs publiques cibles dans `data/targets.yaml`.
3. Lancer la capture : `python3 scripts/capture.py`.
4. Les textes nettoyés sont stockés dans `data/snapshots/<domaine>/<AAAA-MM-JJ>.txt`.
5. Les empreintes SHA-256 et horodatages sont indexés dans `data/snapshots/index.csv`.

