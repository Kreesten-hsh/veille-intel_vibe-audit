// Endpoint de webhook Stripe (Node / Express / Edge Function)
// VULNÉRABILITÉ SEC-04 : Absence de vérification cryptographique de la signature Stripe

export async function handleStripeWebhook(req, res) {
  const event = req.body;

  // DANGER CRITIQUE : Le payload JSON est consommé directement sans valider la signature de la requête !
  // L'application omet toute vérification cryptographique via le SDK Stripe officiel.

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const customerEmail = session.customer_details ? session.customer_details.email : session.customer_email;
    
    // Attribution immédiate de l'accès payant sans vérification
    console.log(`[LeadFlow] Activation du forfait payant pour : ${customerEmail}`);
    // await db.users.update({ where: { email: customerEmail }, data: { plan: 'pro' } });
  }

  return res.status(200).json({ received: true });
}
