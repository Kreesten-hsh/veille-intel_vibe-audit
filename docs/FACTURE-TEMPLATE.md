# Modèle Générique de Facture (Prestation de Services)

> **Document public de référence — Veille-Intel & Vibe-Audit**
> Ce modèle sert de base pour la génération des factures. Il ne contient aucune donnée bancaire réelle, adresse privée ou numéro fiscal personnel. Compléter les champs entre crochets et supprimer les prestations non vendues avant émission.

---

```markdown
================================================================================
                                    FACTURE
================================================================================

Numéro de facture : FACT-2026-XXXX
Date d'émission    : [JJ/MM/AAAA]
Date d'exécution   : [JJ/MM/AAAA]
Échéance           : [À réception / date d'échéance convenue]

--------------------------------------------------------------------------------
ÉMETTEUR (PRESTATAIRE)
--------------------------------------------------------------------------------
Nom / Raison Sociale : [Identité légale exacte de l'émetteur]
                       (L'identité indiquée devra correspondre à celle
                        associée à l'identifiant fiscal utilisé)
Statut               : [Statut juridique / consultant indépendant]
Identifiant fiscal   : [Identifiant fiscal / IFU à compléter selon l'immatriculation]
Adresse              : [Adresse professionnelle ou légale de l'émetteur]
Email                : [Email professionnel de contact]

--------------------------------------------------------------------------------
DESTINATAIRE (CLIENT)
--------------------------------------------------------------------------------
Nom du client / Raison Sociale : [Nom du client ou raison sociale]
Forme juridique / Immatriculation : [SIREN / SIRET ou numéro d'enregistrement légal]
Numéro de TVA intracommunautaire: [Numéro de TVA si assujetti]
Adresse                         : [Adresse légale ou siège du client]
Contact                         : [Nom du signataire ou de l'interlocuteur]

--------------------------------------------------------------------------------
DÉSIGNATION DES PRESTATIONS
--------------------------------------------------------------------------------
(Conserver uniquement la ligne correspondant à la prestation vendue
 et supprimer les autres prestations avant émission)

Désignation                                      Qté   Prix Unit. HT   Total HT
--------------------------------------------------------------------------------
[Option 1] Veille-Intel — Offre Pionnier          1       399,00 €     399,00 €
Abonnement mensuel de veille concurrentielle
hebdomadaire en marque blanche (jusqu'à 5
concurrents, rapport sourcé et recommandations)

[Option 2] Veille-Intel — Offre Standard          1       499,00 €     499,00 €
Abonnement mensuel de veille concurrentielle
hebdomadaire en marque blanche (tarif standard)

[Option 3] Vibe-Audit — Offre Pilote Express      1        99,00 €      99,00 €
Audit de sécurité express d'application IA /
no-code (pilote, rapport complet, preuves
reproductibles, prompts de fix, re-contrôle J+14)

[Option 4] Vibe-Audit — Audit Standard            1       249,00 €     249,00 €
Audit express de sécurité d'application IA /
no-code (rapport 48h, 7 axes de contrôle,
preuves reproductibles, prompts de fix, re-contrôle)

[Option 5] Vibe-Audit — Audit avec Restitution    1       399,00 €     399,00 €
Audit de sécurité complet, rapport sous 48h,
session de restitution de 30 à 45 minutes,
prompts de correction et re-contrôle à J+14
--------------------------------------------------------------------------------
                                              Total Net HT :         [XXX,00] €
                                                       TVA :         [X,XX] €
                                           TOTAL TTC À PAYER :         [XXX,00] €
--------------------------------------------------------------------------------

Traitement fiscal et TVA :
[Traitement fiscal et mention TVA à confirmer avant émission]

(Ne pas utiliser l'article 293 B du CGI comme mention automatique.
 N'inscrire aucune exonération, aucun taux ni aucune mention d'autoliquidation
 tant que le statut fiscal de l'émetteur et celui du client ne sont pas validés.)

================================================================================
MODALITÉS DE RÈGLEMENT
================================================================================
Règlement par virement bancaire.

Coordonnées bancaires pour le virement :
  Titulaire du compte : [Titulaire légal du compte bancaire]
  Banque              : [Nom de l'établissement bancaire]
  Adresse banque      : [Adresse de l'établissement bancaire]
  IBAN                : [IBAN à compléter]
  BIC / SWIFT         : [BIC / SWIFT à compléter]
  Référence virement  : [Référence obligatoire à rappeler lors du virement]

CONDITIONS LÉGALES ET PÉNALITÉS :
- Aucun escompte consenti pour paiement anticipé.
- En cas de retard de paiement, pénalité de retard exigible calculée selon le taux légal
  applicable ou le taux de refinancement de la BCE majoré de 10 points de pourcentage.
- Pour les clients professionnels, indemnité forfaitaire pour frais de recouvrement
  en cas de retard de paiement : 40,00 € (art. D. 441-5 du Code de commerce, si applicable).
```
