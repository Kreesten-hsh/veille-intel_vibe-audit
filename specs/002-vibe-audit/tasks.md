# Tâches d'Exécution : Vibe-Audit

- [ ] **Phase 1 : Formalisation des Modèles & Contrats**
  - [x] T1.1 : Rédiger la spécification produit complète ([`specs/002-vibe-audit/spec.md`](file:///home/hasashi/Bureau/veille-intel_vibe-audit/specs/002-vibe-audit/spec.md)).
  - [x] T1.2 : Rédiger le contrat type d'autorisation et accord de confidentialité NDA ([`templates/vibe-audit/accord-consentement.md`](file:///home/hasashi/Bureau/veille-intel_vibe-audit/templates/vibe-audit/accord-consentement.md)).
  - [x] T1.3 : Créer le gabarit HTML/CSS de rapport exécutif 48h ([`templates/vibe-audit/rapport.html.j2`](file:///home/hasashi/Bureau/veille-intel_vibe-audit/templates/vibe-audit/rapport.html.j2)).

- [ ] **Phase 2 : Application Témoin Réaliste & Outillage**
  - [x] T2.1 : Développer l'application témoin réaliste simulant une app Lovable/Bolt vulnérable (Supabase RLS bypass, Stripe webhook non signé, clé exposée).
  - [x] T2.2 : Rédiger le script de génération du rapport d'exemple basé sur l'app témoin ([`scripts/render_report.py`](file:///home/hasashi/Bureau/veille-intel_vibe-audit/scripts/render_report.py)).

- [ ] **Phase 3 : Prospection Asynchrone & Lancement des Pilotes**
  - [ ] T3.1 : Sourcer 20 fondateurs de projets Lovable/Bolt récents sur X (#buildinpublic) et LinkedIn.
  - [ ] T3.2 : Envoyer les 10 premiers messages d'invitation au Pilote à 99 € avec lien vers l'accord et exemple d'audit.
  - [ ] T3.3 : Clôturer les 2 audits pilotes à 99 € avant le 24 octobre.
