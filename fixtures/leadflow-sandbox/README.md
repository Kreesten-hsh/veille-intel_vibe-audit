# LeadFlow Sandbox (Cible Fictive de Test & Démonstration)

> **AVERTISSEMENT :** Cette application est une cible de démonstration fictive et contrôlée (`leadflow-demo.example`), conçue spécifiquement pour servir de banc d'essai reproductible et sans risque pour Vibe-Audit. Toutes les données sont générées et fictives.

---

## 1. Présentation de la Cible
**LeadFlow** simule une application SaaS B2B de gestion de prospects et commandes créée typiquement avec un outil d'assistance IA (Lovable / Bolt / Cursor), utilisant un backend Supabase, des notifications email Resend et des règlements par Stripe.

---

## 2. Les 4 Failles Types Reproduites

### SEC-01 : Fuite de Base de Données par RLS Manquant (Supabase)
- **Localisation :** `supabase/schema.sql` et endpoint `/rest/v1/orders`
- **Gravité :** Élevée (OWASP WSTG-ATHZ-02 & OWASP API1:2023 - BOLA)
- **Manifestation :** La table `orders` n'a pas la Row Level Security activée (`ALTER TABLE orders ENABLE ROW LEVEL SECURITY;` manquant).
- **Conséquence :** Tout utilisateur disposant de la clé publique `anon` peut requêter l'API REST et extraire la totalité des 142 commandes sans authentification (`Content-Range: 0-1/142`).

### SEC-02 : Clé API Secrète Resend Exposée Côté Client
- **Localisation :** `src/config.ts` et `src/lib/resend.ts`
- **Gravité :** Élevée
- **Manifestation :** La clé privée de production (`re_live_...`) est embarquée dans le code front-end client-side sous la variable `VITE_RESEND_API_KEY` au lieu d'être confinée sur un serveur ou une Supabase Edge Function.
- **Conséquence :** N'importe quel visiteur inspectant les bundles JS peut usurper le domaine expéditeur et envoyer des campagnes frauduleuses.

### SEC-03 : En-têtes HTTP de Sécurité Manquants & CORS Permissif
- **Localisation :** `server.py` (configuration HTTP)
- **Gravité :** Faible à Moyenne
- **Manifestation :** Absence des en-têtes `Content-Security-Policy` (CSP) et `X-Frame-Options`, et en-tête `Access-Control-Allow-Origin: *` permissif.
- **Conséquence :** Risque de clickjacking par intégration en iframe et vulnérabilité aux attaques XSS.

### SEC-04 : Webhook Stripe Non Signé
- **Localisation :** `api/stripe-webhook.js` et route `/api/webhooks/stripe`
- **Gravité :** Élevée
- **Manifestation :** La fonction traite le payload entrant JSON directement sans appeler `stripe.webhooks.constructEvent()` avec le secret de signature `whsec_...`.
- **Conséquence :** N'importe quel attaquant peut envoyer un faux événement HTTP POST `checkout.session.completed` pour débloquer un abonnement sans payer.

---

## 3. Lancement Local du Serveur de Test

Le serveur de simulation utilise exclusivement la bibliothèque standard Python (aucun paquet externe requis) :

```bash
# Démarrage du serveur mock (port 8765 par défaut)
python3 fixtures/leadflow-sandbox/server.py

# Test de la commande curl de preuve (reproduit exactement le constat SEC-01)
curl -i "http://localhost:8765/rest/v1/orders?select=id,customer_email,amount&limit=2" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fictif_anon_key"
```
