#!/usr/bin/env python3
import csv, difflib, hashlib, re, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import httpx

try:
    import yaml
except ImportError:
    yaml = None

USER_AGENT = "veille-intel-bot (contact : akreesten@gmail.com)"
DELAY = 5.0
_last_fetch: dict[str, float] = {}

def is_allowed(url: str, client: httpx.Client) -> bool:
    parsed = urlparse(url)
    rp = RobotFileParser()
    try:
        resp = client.get(f"{parsed.scheme}://{parsed.netloc}/robots.txt", timeout=10.0)
        if resp.status_code == 200:
            rp.parse(resp.text.splitlines())
        else:
            return True
    except Exception:
        return True
    return rp.can_fetch(USER_AGENT, url)

def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    return "\n".join(line.strip() for line in soup.get_text().splitlines() if line.strip())

def save_snapshot_and_diff(url: str, content: str, out_dir: Path = Path("data/snapshots")) -> dict:
    parsed = urlparse(url)
    domain = parsed.netloc or "unknown_domain"
    path_clean = parsed.path.strip("/")
    slug = re.sub(r"[^\w\-]+", "_", path_clean).strip("_")

    domain_dir = out_dir / domain
    target_dir = domain_dir / slug if slug else domain_dir
    target_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
    today_snapshot = target_dir / f"{today}.txt"

    # Récupération du snapshot précédent pour diff N vs N-1
    candidates = sorted([
        f for f in target_dir.glob("*.txt")
        if not f.name.endswith(".diff.txt") and f.name != f"{today}.txt"
    ])

    prev_content = None
    prev_filename = None
    if candidates:
        prev_file = candidates[-1]
        prev_content = prev_file.read_text(encoding="utf-8")
        prev_filename = prev_file.name
    elif today_snapshot.exists():
        prev_content = today_snapshot.read_text(encoding="utf-8")
        prev_filename = f"{today}.txt"

    changed = False
    diff_path = None
    if prev_content is not None and prev_content != content:
        diff_lines = list(difflib.unified_diff(
            prev_content.splitlines(keepends=True),
            content.splitlines(keepends=True),
            fromfile=prev_filename,
            tofile=f"{today}.txt",
        ))
        if diff_lines:
            diff_file = target_dir / f"{today}.diff.txt"
            diff_file.write_text("".join(diff_lines), encoding="utf-8")
            changed = True
            diff_path = str(diff_file)

    # Écriture du snapshot du jour
    today_snapshot.write_text(content, encoding="utf-8")

    # Rétrocompatibilité : conservation d'une copie à la racine du domaine si URL avec chemin
    if slug:
        domain_dir.mkdir(parents=True, exist_ok=True)
        (domain_dir / f"{today}.txt").write_text(content, encoding="utf-8")

    # Mise à jour de index.csv
    out_dir.mkdir(parents=True, exist_ok=True)
    index_csv = out_dir / "index.csv"
    write_header = not index_csv.exists()
    with open(index_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["url", "date", "sha256"])
        writer.writerow([url, today, sha256])

    return {
        "sha256": sha256,
        "changed": changed,
        "diff_path": diff_path,
    }

def capture_url(url: str, client: httpx.Client, out_dir: Path = Path("data/snapshots")) -> str | None:
    domain = urlparse(url).netloc
    elapsed = time.time() - _last_fetch.get(domain, 0.0)
    if elapsed < DELAY:
        time.sleep(DELAY - elapsed)
    _last_fetch[domain] = time.time()
    if not is_allowed(url, client):
        print(f"[IGNORÉ] robots.txt interdit : {url}")
        return None
    try:
        resp = client.get(url, timeout=15.0)
        if resp.status_code in (401, 403, 429):
            print(f"[BLOCAGE {resp.status_code}] Accès restreint ou protégé : {url}")
            return None
        resp.raise_for_status()
    except Exception as e:
        print(f"[ERREUR] Échec de capture pour {url} : {e}")
        return None
    text = extract_text(resp.text)
    res = save_snapshot_and_diff(url, text, out_dir=out_dir)
    sha256 = res["sha256"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[SUCCÈS] {url} -> {today}.txt ({sha256[:8]}...)")
    return sha256

def load_targets(path: Path = Path("data/targets.yaml")) -> list[dict]:
    if not path.exists():
        return []
    if yaml is not None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict) and "targets" in data:
                items = data["targets"]
            elif isinstance(data, list):
                items = data
            else:
                items = []
            results = []
            for item in items:
                if isinstance(item, dict) and "url" in item:
                    results.append(item)
                elif isinstance(item, str):
                    results.append({"url": item})
            if results:
                return results
        except Exception:
            pass
    targets, current = [], {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            if current and "url" in current:
                targets.append(current)
            current, line = {}, line[2:].strip()
        if ":" in line:
            k, v = line.split(":", 1)
            current[k.strip()] = v.strip().strip("\"'")
    if current and "url" in current:
        targets.append(current)
    return targets

def main():
    targets = load_targets()
    if not targets:
        print("Aucune cible trouvée dans data/targets.yaml")
        return
    headers = {"User-Agent": USER_AGENT}
    with httpx.Client(headers=headers, follow_redirects=True) as client:
        for t in targets:
            url = t.get("url") if isinstance(t, dict) else str(t)
            if url:
                capture_url(url, client)

if __name__ == "__main__":
    main()

