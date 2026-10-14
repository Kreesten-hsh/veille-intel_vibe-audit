#!/usr/bin/env python3
"""Script de rendu du rapport Vibe-Audit à partir d'un fichier JSON."""
import json
import shutil
import subprocess
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def render_report(json_path: str, html_out: str, template_type: str | None = None) -> None:
    data_file = Path(json_path)
    output_html = Path(html_out)

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Détection automatique du gabarit (vibe-audit ou veille-intel)
    chosen_template = template_type
    if not chosen_template:
        if "signals" in data:
            chosen_template = "veille-intel"
        else:
            chosen_template = "vibe-audit"

    template_dir = Path(__file__).resolve().parent.parent / "templates" / chosen_template
    if not template_dir.exists():
        template_dir = Path(__file__).resolve().parent.parent / "templates" / "vibe-audit"

    env = Environment(loader=FileSystemLoader(str(template_dir)), autoescape=True)
    template = env.get_template("rapport.html.j2")
    rendered_html = template.render(**data)

    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(rendered_html, encoding="utf-8")
    print(f"Rapport HTML généré ({chosen_template}) : {output_html}")

    output_pdf = output_html.with_suffix(".pdf")
    pdf_generated = False

    # 1. Tentative via WeasyPrint
    try:
        import weasyprint
        weasyprint.HTML(string=rendered_html, base_url=str(output_html.parent)).write_pdf(str(output_pdf))
        print(f"Rapport PDF généré (WeasyPrint) : {output_pdf}")
        pdf_generated = True
    except ImportError:
        pass
    except Exception as e:
        print(f"[AVERTISSEMENT] Erreur WeasyPrint lors du rendu PDF : {e}", file=sys.stderr)

    # 2. Rebond direct via Chrome / Chromium headless si disponible
    if not pdf_generated:
        chrome_bin = (
            shutil.which("google-chrome")
            or shutil.which("chromium")
            or shutil.which("chromium-browser")
        )
        if chrome_bin:
            cmd = [
                chrome_bin,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                "--no-pdf-header-footer",
                f"--print-to-pdf={output_pdf}",
                f"file://{output_html.resolve()}",
            ]
            res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if res.returncode == 0 and output_pdf.exists():
                print(f"Rapport PDF généré ({chrome_bin}) : {output_pdf}")
                pdf_generated = True

    if not pdf_generated:
        print("Export PDF différé : ouvrez le fichier HTML dans votre navigateur et sélectionnez 'Imprimer en PDF'.")

if __name__ == "__main__":
    args = sys.argv[1:]
    template_flag = None
    positional_args = []

    i = 0
    while i < len(args):
        if args[i] == "--template" and i + 1 < len(args):
            template_flag = args[i + 1]
            i += 2
        elif args[i].startswith("--template="):
            template_flag = args[i].split("=", 1)[1]
            i += 1
        else:
            positional_args.append(args[i])
            i += 1

    src_json = positional_args[0] if len(positional_args) > 0 else "fixtures/leadflow-sandbox/audit-data.json"
    dest_html = positional_args[1] if len(positional_args) > 1 else "output/leadflow-report.html"
    render_report(src_json, dest_html, template_type=template_flag)
