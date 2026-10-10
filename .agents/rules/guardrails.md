---
trigger: always_on
description: Règles non négociables du projet
---

1. Avant toute tâche, lis docs/00-CONTEXTE.md.
2. Zéro dépense : aucun service payant, aucune clé payante, aucun essai exigeant une carte. Si une tâche l'exige, arrête-toi et dis-le.
3. Légalité : aucune analyse d'une cible sans consentement écrit enregistré. Sources publiques uniquement, robots.txt respecté, aucun contournement de login, de CAPTCHA ou d'anti-bot.
4. Jamais d'envoi automatique de messages. L'agent prépare, l'humain envoie.
5. Aucun secret ni donnée client dans git. .env ignoré. Fixtures de test fictives.
6. Aucun chiffre, aucune source, aucune fonctionnalité inventés. Distingue fait et interprétation. Ce que tu ne peux pas vérifier : "non vérifié".
7. Aucune intégration Stripe, PayPal, Payoneer ou Wise.
8. Sélectionne et charge proactivement (via view_file) les 1 à 3 skills les plus adaptés à chaque tâche dès la réception du prompt, sans attendre de préfixe "/".
9. Si une exigence est ambiguë, pose la question. Une branche et un commit clair par changement. Tests avant "terminé".