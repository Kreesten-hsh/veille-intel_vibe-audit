#!/usr/bin/env python3
"""Script de rendu du rapport Vibe-Audit à partir d'un fichier JSON."""
import json
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def render_report(json_path: str, html_out: str) -> None:
    data_file = Path(json_path)
    output_html = Path(html_out)
    template_dir = Path(__file__).resolve().parent.parent / "templates" / "vibe-audit"

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader(str(template_dir)), autoescape=True)
    template = env.get_template("rapport.html.j2")
    rendered_html = template.render(**data)

    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(rendered_html, encoding="utf-8")
    print(f"Rapport HTML généré : {output_html}")

    output_pdf = output_html.with_suffix(".pdf")
    try:
        import weasyprint
        weasyprint.HTML(string=rendered_html, base_url=str(output_html.parent)).write_pdf(str(output_pdf))
        print(f"Rapport PDF généré : {output_pdf}")
    except ImportError:
        print("WeasyPrint n'est pas installé dans l'environnement Python. Export PDF ignoré (aucun paquet système installé).")

if __name__ == "__main__":
    src_json = sys.argv[1] if len(sys.argv) > 1 else "work/echantillon-data.json"
    dest_html = sys.argv[2] if len(sys.argv) > 2 else "output/reports/echantillon-vibe-audit.html"
    render_report(src_json, dest_html)
