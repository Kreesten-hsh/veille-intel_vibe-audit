-- LeadFlow Mock Schema (Généré pour reproduction contrôlée de failles de sécurité)
-- ATTENTION : Ce schéma omet volontairement l'activation du RLS sur 'orders' pour simuler la faille SEC-01.

-- Table des utilisateurs (avec RLS activé pour comparaison)
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Utilisateurs ne voient que leur profil"
    ON users FOR SELECT
    USING (auth.uid() = id);

-- Table des commandes (VULNÉRABLE : RLS NON ACTIVÉ)
-- L'instruction d'activation de la sécurité au niveau des lignes est totalement omise sur cette table
CREATE TABLE IF NOT EXISTS orders (
    id TEXT PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    customer_email TEXT NOT NULL,
    amount INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'completed',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Données d'exemple fictives de test
INSERT INTO orders (id, user_id, customer_email, amount, status) VALUES
('ord_812', 'a0000000-0000-0000-0000-000000000001', 'm.***@gmail.com', 4900, 'completed'),
('ord_813', 'a0000000-0000-0000-0000-000000000002', 'agence.***@pro.fr', 12900, 'completed')
ON CONFLICT (id) DO NOTHING;
