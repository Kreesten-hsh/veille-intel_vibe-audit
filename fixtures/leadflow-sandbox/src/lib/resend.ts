// Client de notification email appelé directement depuis le front-end React
// Anti-pattern fréquent sur les applications générées par Lovable / Bolt sans backend
import { CONFIG } from "../config";

export async function sendWelcomeEmail(to: string, userName: string) {
  // DANGER : Appel d'API avec clé privée directement depuis le navigateur
  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${CONFIG.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: "LeadFlow <notifications@leadflow-demo.example>",
      to: [to],
      subject: "Bienvenue sur LeadFlow",
      html: `<p>Bonjour ${userName}, votre compte a bien été activé.</p>`,
    }),
  });

  return response.json();
}
