# Operations Plan: Vibe-Audit

## 1. Operating Cycle (48-Hour SLA Timeline)

| Heure | Étape | Actions Opérateur | Livrable |
| :--- | :--- | :--- | :--- |
| **H0 - H2** | **Onboarding & Légal** | Réception de la commande. Signature du formulaire de consentement écrit et du NDA. Vérification des accès staging ou URL de prod convenue. | Accord signé archivé |
| **H2 - H12** | **Cartographie Passive** | Inspection des headers de sécurité, des requêtes réseau (DevTools), inspection des bundles JS pour détecter d'éventuelles clés API secrètes exposées, tests passifs d'authentification. | Fiche de collecte brute |
| **H12 - H24** | **Tests Ciblés de Logique** | Vérification de l'isolation des données (test d'accès non autorisé à des ressources d'autres utilisateurs - IDOR), analyse des permissions Supabase/Firebase (Row Level Security). | Preuves reproductibles validées |
| **H24 - H36** | **Génération & Test des Prompts** | Rédaction des prompts correctifs adaptés à l'outil du client (Lovable/Bolt/Cursor). Test préalable de la syntaxe sur l'environnement de test local (`work/demo-vulnerable-app`). | Prompts de remédiation vérifiés |
| **H36 - H48** | **Finalisation & Livraison** | Assemblage du rapport PDF exécutif, relecture humaine finale, envoi sécurisé par email au client avec invitation au re-check à J+14. | Rapport PDF délivré |
| **J+14** | **Re-Check de Sécurité** | Re-test des endpoints corrigés. Envoi du certificat de conformité mis à jour. | Badge de re-contrôle validé |

## 2. Minimal Tooling Stack (Zero-Spend)
- **Analyse dynamique / Réseau** : Chrome DevTools, Burp Suite Community (version gratuite) ou OWASP ZAP (open-source), `curl`, scripts Python locaux.
- **Analyse statique de code** : Semgrep (version open-source gratuite), ESLint security plugins.
- **Environnement de validation** : `work/demo-vulnerable-app` (application vulnérable locale existante pour valider les patterns d'attaque et de remédiation).
- **Facturation & Règlements** : Compte Moneco (virements SEPA) ou Ecobank.

## 3. Legal & Compliance Guardrails (Crucial)
1. **Consentement Écrit Préalable Enregistré** : Aucune URL ni ligne de code n'est analysée sans formulaire signé électroniquement par le propriétaire légitime.
2. **Périmètre Strict Non-Intrusif** : Aucun déni de service (DoS), aucun brute-force destructif, aucun accès aux infrastructures tierces (Stripe, hébergeurs cloud).
3. **Destruction des données post-audit** : Suppression de toutes les données et accès temporaires à l'issue du re-contrôle à J+14.
