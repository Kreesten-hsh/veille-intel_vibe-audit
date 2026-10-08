# Protocole de Consentement et d'Autorisation d'Audit Technique

---

**Ce document doit être obligatoirement complété, paraphé et signé par le propriétaire légitime de l'application avant toute intervention de diagnostic.**

---

### 1. Parties Prenantes

#### Le Client (Commanditaire)
- **Nom et Prénom :** [NOM ET PRÉNOM DU SIGNATAIRE]
- **Qualité / Titre :** [Fondateur / CEO / CTO / Représentant légal habilité]
- **Nom du Projet / Société :** [NOM DE L'APPLICATION OU DÉNOMINATION COMMERCIALE]
- **Adresse Email de Contact :** [EMAIL DU SIGNATAIRE]
- **Déclaration sur l'honneur :** Le signataire atteste sur l'honneur détenir la propriété intellectuelle légitime ou un mandat d'administration exprès sur le code source et les infrastructures désignées ci-dessous.

#### Le Prestataire (Auditeur)
- **Nom et Prénom :** Kreesten
- **Qualité :** Consultant indépendant en sécurité des systèmes informatiques
- **Email professionnel :** [EMAIL PROFESSIONNEL]

---

### 2. Périmètre Technique Autorisé

L'autorisation d'audit express (Vibe-Audit) est strictement circonscrite aux éléments techniques suivants :

1. **Code source :**
   - Dépôt Git en lecture seule ou archive ZIP : `[URL DU DÉPÔT OU NOM DU FICHIER ZIP]`
   - Branche autorisée : `[main / production / staging]`
2. **URL publique de l'application :**
   - `[https://app.monprojet.com]` (Requêtes passives d'inspection des en-têtes et de la configuration CORS uniquement).
3. **Schémas et politiques de sécurité de base de données :**
   - Fichiers de migrations et d'export SQL fournis par le client (ex. schéma public et politiques Supabase RLS).

*Tout actif, sous-domaine, serveur tiers ou service non expressément mentionné dans ce tableau est formellement exclu du périmètre.*

---

### 3. Fenêtre Temporelle d'Intervention

- **Date et heure de début d'autorisation :** [JJ/MM/AAAA à 09h00]
- **Date et heure d'expiration de l'autorisation :** [JJ/MM/AAAA à 18h00] (48 heures ouvrées max)

Au-delà de cette fenêtre temporelle, la présente autorisation devient caduque de plein droit.

---

### 4. Engagements Déontologiques et Limites Techniques

1. **Caractère passif et non destructif :** L'audit se limite à l'analyse statique du code source, à l'inspection syntaxique des scripts de base de données et à des requêtes passives de validation de configuration.
2. **Interdiction d'attaques actives :** Le prestataire s'interdit formellement tout test d'intrusion destructif, toute attaque par déni de service (DoS/DDoS), toute altération de données ou injection de code hostile.
3. **Arrêt d'urgence en cas d'exposition de données réelles :** Si lors du contrôle d'une règle RLS, une vulnérabilité expose des données réelles d'utilisateurs finaux, le prestataire s'engage à interrompre immédiatement son intervention, à ne copier aucune donnée personnelle et à avertir le client sans délai en privé.
4. **Confidentialité et destruction des copies locales :** Le prestataire s'engage à ne divulguer aucun extrait du code source à des tiers, à n'utiliser aucun service d'API externe, et à détruire définitivement l'ensemble des copies locales et archives de travail au plus tard 30 jours après remise du rapport final.

---

### 5. Signature et Accord Formel

Fait à : `[LIEU]`  
Le : `[DATE]`  

**Pour le Client (Commanditaire) :**  
*Mention manuscrite obligatoire : « Lu et approuvé, bon pour autorisation d'audit express dans le périmètre défini ci-dessus »*  

Signature :  
`[SIGNATURE ÉLECTRONIQUE OU NUMÉRISÉE]`  


**Pour le Prestataire :**  
Kreesten, Consultant indépendant  

Signature :  
`[SIGNATURE PRESTATAIRE]`
