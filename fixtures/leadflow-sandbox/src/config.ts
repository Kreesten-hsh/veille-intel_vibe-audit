// Configuration front-end client (Vite / React)
// VULNÉRABILITÉ SEC-02 : Clé secrète Resend exposée dans les variables d'environnement client-side

export const CONFIG = {
  SUPABASE_URL: "https://leadflow-demo.example",
  SUPABASE_ANON_KEY: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxlYWRmbG93Iiwicm9sZSI6ImFub24ifQ.fictif_anon_key",
  // DANGER : Clé secrète de production exposée dans le bundle public !
  // Devrait être isolée dans une Supabase Edge Function ou route serveur dédiée.
  RESEND_API_KEY: "re_live_9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d",
  STRIPE_PUBLIC_KEY: "pk_test_TYooMQauvdEDq54NiTphI7jx",
};
