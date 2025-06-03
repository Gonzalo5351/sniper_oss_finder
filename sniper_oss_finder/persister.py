# src/persister.py
from pathlib import Path
import json

FOLLOWED_PATH = Path("data/followed.json")
FOLLOWED_PATH.parent.mkdir(parents=True, exist_ok=True)

def save_followed_repos(repos: list[dict]) -> None:
    """
    Save selected repositories to a local JSON file, avoiding duplicates.
    """
    if not repos:
        return

    existing = []
    if FOLLOWED_PATH.exists():
        try:
            with open(FOLLOWED_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Error decoding existing followed.json. Overwriting.")

    existing_names = {repo["full_name"] for repo in existing if "full_name" in repo}
    new_repos = [r for r in repos if r.get("full_name") not in existing_names]

    if not new_repos:
        print("ℹ️ All selected repos are already being followed.")
        return

    all_repos = existing + new_repos

    with open(FOLLOWED_PATH, "w", encoding="utf-8") as f:
        json.dump(all_repos, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved {len(new_repos)} new repo(s) to follow-up list.")
