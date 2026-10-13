# Operations Plan: Veille-Intel

## 1. Weekly Operating Cycle

| Day | Focus | Core Activities | Deliverable |
| :--- | :--- | :--- | :--- |
| **Lundi (07h30 - 08h30)** | **Livraison & Client SLA** | Envoi des PDFs aux agences partenaires avant 08h30. Traitement des accusés de réception. | Rapports livrés dans l'inbox des directeurs |
| **Mardi (09h00 - 13h00)** | **Capture & Scraping** | Exécution des scripts de capture de diffs sur les 5 sites concurrents par client (pricing, changelogs, blogs, pages carrières). | Snapshots et logs bruts horodatés |
| **Mercredi (09h00 - 14h00)** | **Extraction & Triage** | Filtrage du bruit (CSS/typos éliminés), extraction des 5 à 8 signaux stratégiques majeurs, rédaction du premier jet d'analyse. | Brouillon structuré |
| **Jeudi (09h00 - 12h00)** | **Fact-Checking & Relecture** | Contrôle humain strict de chaque source, vérification des liens publics, validation des 3 recommandations. | Fiche validée "Zero Hallucination" |
| **Vendredi (09h00 - 12h00)** | **Mise en page & Marque Blanche** | Génération des PDFs aux couleurs des agences clientes, contrôle qualité typographique. | Fichiers PDF finaux prêts pour lundi |
| **Samedi / Dimanche** | **Repos & Astreinte légère** | Veille passive sur annonces majeures de week-end si besoin. | - |

## 2. Minimal Tooling Stack (Compliant with Zero-Spend Guardrail)

1. **Moteur d'inspection & de capture** : Scripts Python locaux (`httpx`, `beautifulsoup4`, `playwright-cli` headless pour les pages dynamiques). Gratuit, local.
2. **Moteur de synthèse & assistance rédactionnelle** : Abonnements existants (Google AI Pro / ChatGPT Plus). Coût marginal externe additionnel : 0 €.
3. **Moteur de compilation PDF** : `reportlab` ou templates HTML/CSS convertis via headless Chrome / WeasyPrint. Rendu ultra-propre, aucune dépendance payante.
4. **Gestion financière & facturation** : Compte Moneco (IBAN européen pour réceptions SEPA sans friction pour l'agence) + compte Ecobank (Bénin).
5. **Messagerie B2B** : Client email professionnel direct (SMTP/IMAP) pour envois artisanaux 1-to-1.

## 3. Standard Operating Procedures (SOPs)

### SOP 1 : Le Filtre "Zero Hallucination" (Jeudi 10h00)
1. Prendre chaque signal rédigé dans le rapport hebdomadaire.
2. Cliquer manuellement sur l'URL source publique enregistrée.
3. Vérifier que la date de modification correspond bien aux 7 derniers jours.
4. Valider que la citation ou le chiffre est textuellement exact. Si une incertitude subsiste, marquer obligatoirement *"Information non vérifiée / estimation"* ou supprimer le signal.

### SOP 2 : Livraison du Lundi Matin (Lundi 07h45)
1. Ouvrir le dossier des livrables de la semaine (`output/week-<date>/`).
2. Vérifier la présence du logo de l'agence sur la première page et la conformité du code couleur.
3. Rédiger un email d'accompagnement de 3 lignes : le lien vers le PDF, les 3 faits saillants de la semaine résumés en 1 phrase chacun.
4. Envoyer manuellement avant 08h30 CET avec accusé de lecture.

### SOP 3 : Gestion d'une Question ou Demande de Précision de l'Agence
1. Répondre sous un délai maximum de 2 heures ouvrées.
2. Si la demande concerne un détail technique d'un concurrent, fournir la capture d'écran horodatée brute de la source publique.
3. Rappeler poliment le cadre du contrat : aucune recherche ad-hoc sur-mesure hors des 5 concurrents définis, mais intégration possible de la suggestion dans le radar de la semaine suivante.

## 4. Legal, Tax & Compliance Checklist

- [x] **Conformité Scraping & Collecte** : Analyse exclusive de contenus web publiquement accessibles, respect du `robots.txt`, aucune tentative de contournement de CAPTCHA, aucun accès à des zones nécessitant un login ou un compte privé.
- [ ] **Statut Fiscal & Facturation** : Déclaration des revenus freelance auprès de l'administration fiscale au Bénin (IFU - Identifiant Fiscal Unique). Factures établies en devises (Euros) avec mention légale de dispense de TVA selon les règles internationales d'exportation de services B2B.
- [ ] **Protection des données & Confidentialité** : La liste des 5 concurrents fournie par chaque agence est strictement confidentielle et ne fait l'objet d'aucun partage ni revente.
