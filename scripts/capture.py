#!/usr/bin/env python3
import csv, hashlib, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import httpx

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
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sha256 = hashlib.sha256(text.encode("utf-8")).hexdigest()
    domain_dir = out_dir / domain
    domain_dir.mkdir(parents=True, exist_ok=True)
    (domain_dir / f"{today}.txt").write_text(text, encoding="utf-8")
    index_csv = out_dir / "index.csv"
    write_header = not index_csv.exists()
    with open(index_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["url", "date", "sha256"])
        writer.writerow([url, today, sha256])
    print(f"[SUCCÈS] {url} -> {today}.txt ({sha256[:8]}...)")
    return sha256

def load_targets(path: Path = Path("data/targets.yaml")) -> list[dict]:
    if not path.exists():
        return []
    targets, current = [], {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
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
