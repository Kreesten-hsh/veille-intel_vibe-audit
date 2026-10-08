# Scripts de Prospection et Réponses Objections

> **Règle absolue (Garde-fous #3) :** Aucun envoi automatique. L'agent prépare ou fournit les trames, l'humain personnalise manuellement chaque message, vérifie la pertinence du destinataire et clique sur envoyer.

---

## 1. Veille-Intel (Agences Marketing)

### Message Initial (Prise de contact directe)
**Objet :** Veille concurrentielle marque blanche pour vos clients chez [Nom de l'agence]

Bonjour [Prénom ou Nom du dirigeant],

J'ai remarqué l'expertise de [Nom de l'agence] en accompagnement stratégique pour vos clients B2B.

Beaucoup d'agences souhaitent proposer une veille hebdomadaire sur les concurrents directs de leurs clients (mouvements de pricing, lancements d'offres, recrutements clés, pivots de positionnement), mais n'ont pas la bande passante interne pour affecter un analyste à cette tâche.

Je produis ce service de façon externalisée et 100 % marque blanche :
- Chaque lundi matin, vous recevez un PDF soigné de 3 à 5 pages sans aucune mention de mon côté, prêt à être envoyé à votre client.
- 5 à 10 signaux concrets vérifiés, avec URL source, date de capture, faits observés et 3 recommandations d'actions.
- Aucune invention : si un concurrent ne bouge pas, le rapport le mentionne clairement.

L'offre démarre à 399 € / mois pour les 3 premières agences partenaires.

Seriez-vous ouvert à un échange de 10 minutes cette semaine pour voir un exemple de rapport type ?

Bien cordialement,  
[Votre Prénom Nom]  
[Votre Téléphone / Lien Calendly ou email]  
*Si vous ne souhaitez plus recevoir de message de ma part, répondez simplement « STOP » et vos coordonnées seront immédiatement retirées de ma liste.*

---

### Relance Unique (J+4 ou J+5 ouvrés)
**Objet :** Re: Veille concurrentielle marque blanche pour vos clients chez [Nom de l'agence]

Bonjour [Prénom ou Nom],

Je me permets une brève relance suite à mon message de la semaine passée au sujet de la veille concurrentielle marque blanche.

Pour vous faire gagner du temps : si vous avez un client pour lequel vous aimeriez tester la pertinence des signaux sur 5 de ses concurrents, je peux vous envoyer un aperçu de la structure du rapport par retour d'email.

Dans le cas contraire, aucun problème, je ne vous relancerai plus.

Bonne continuation,  
[Votre Prénom Nom]

---

### Réponse à l'objection : « Pourquoi payer alors qu'on peut utiliser une IA gratuite (ChatGPT, Perplexity) ? »

> « C'est une excellente question. Les pages suivies sont publiques. Aucune donnée client n'est transmise à un service tiers. L'analyse est rédigée et vérifiée par un humain. Cependant, il y a trois différences fondamentales entre demander à ChatGPT de faire une veille et notre livrable :
> 
> 1. **L'ancrage et la traçabilité des faits** : Une IA généraliste hallucine fréquemment des dates ou déforme des tarifs. Notre système capture le code source brut, date chaque observation et conserve la preuve d'archive. Chaque affirmation est sourcée avec une URL active.
> 2. **L'analyse différentielle N vs N-1** : ChatGPT ne sait pas ce que le site affichait la semaine dernière. Nous comparons automatiquement les snapshots de semaine en semaine pour isoler le delta réel (une ligne ajoutée sur une page pricing, une offre d'emploi supprimée).
> 3. **Le temps de vos équipes et la marque blanche** : Même avec un outil gratuit, un de vos consultants doit passer 2 à 3 heures par semaine à vérifier les sources, faire la mise en page et rédiger les recommandations. Nous vous livrons un PDF marque blanche directement diffusable en moins de 45 minutes de validation par votre pôle. »

---

## 2. Vibe-Audit (Fondateurs d'Apps Lovable / Bolt / Cursor)

### Message Initial (Fondateur)
**Objet :** Vérification sécurité express pour [Nom de l'application / URL]

Bonjour [Prénom du fondateur],

J'ai découvert votre application [Nom de l'application] construite récemment via [Lovable / Bolt / Cursor]. Bravo pour le déploiement rapide !

En développant avec des outils d'IA générative, il est fréquent que certains angles morts de sécurité s'installent sans qu'on s'en rende compte :
- Politiques Row Level Security (RLS) manquantes ou trop permissives sur Supabase.
- Clés secrètes ou tokens tiers (OpenAI, Stripe secret) exposés dans le bundle client ou l'historique de version.
- Autorisation de fonctionnalités critiques gérée dans le navigateur plutôt que côté serveur.

Je propose un **audit express en 48h** (formule pilote à 99 € pour les deux premiers projets) :
- Analyse statique et passive 100 % sécurisée (aucun test d'intrusion destructeur, aucune donnée copiée).
- Rapport PDF clair avec pour chaque faille : preuve reproductible, niveau de risque, et le **prompt prêt à coller dans votre outil IA** pour corriger le problème immédiatement.
- Contre-visite de contrôle offerte à J+14.

Pour lancer l'audit, nous signons au préalable un protocole de consentement écrit strict (`consent.md`) garantissant la confidentialité de votre code.

Avez-vous 10 minutes pour échanger par message ou en visio ?

Bien cordialement,  
[Votre Prénom Nom]  
*Pour ne plus être contacté, répondez « OPPOSITION » et vos informations seront supprimées.*

---

### Relance Unique (J+4 ou J+5 ouvrés)
**Objet :** Re: Vérification sécurité express pour [Nom de l'application]

Bonjour [Prénom],

Je me permets de revenir vers vous concernant la sécurité de [Nom de l'application].

Si vous avez déjà passé en revue vos règles RLS et vos clés secrètes, vous êtes déjà dans le haut du panier des créateurs no-code / IA ! Si vous avez un doute, notre pilote à 99 € reste disponible pour un diagnostic complet sous 48h avec les prompts de correction.

Je ne vous dérange pas davantage si le sujet n'est pas prioritaire pour vous actuellement.

Bonne suite dans le développement de votre projet !  
[Votre Prénom Nom]

---

### Réponse à l'objection : « Pourquoi payer alors qu'on peut demander à l'IA (ou au chatbot) d'auditer le code gratuitement ? »

> « Demander à un LLM d'auditer son propre code ou de vérifier une application pose trois limites critiques :
> 
> 1. **L'illusion de sécurité ("complaisance du modèle")** : Les modèles de langage ont tendance à rassurer l'utilisateur et à valider une architecture même trouée, parce qu'ils ne testent pas réellement l'environnement d'exécution ni les migrations SQL réelles.
> 2. **L'angle mort des configurations et de l'historique** : L'IA ne voit que ce que vous lui collez dans la fenêtre de prompt. Elle ne va pas chercher les commits git oubliés contenant un `.env`, ni vérifier l'absence d'en-tête HSTS ou une mauvaise configuration CORS sur votre URL publique en production.
> 3. **La vérification humaine responsable** : Dans notre rapport, chaque constat est reproduit manuellement avant d'être consigné. Nous ne vous vendons pas une liste brute d'alertes fantômes, mais des preuves testées et les prompts exacts pour réparer les failles sans casser votre application. »
