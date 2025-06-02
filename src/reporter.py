# src/reporter.py
from typing import List, Dict
from src.persister import save_followed_repos

def display_report(repos: List[Dict], interactive: bool=True):
    print("\n=== Open Source Opportunities ===\n")

    for idx, repo in enumerate(repos, start=1):
        print(f"[{idx}] {repo.get('name', 'N/A')}")
        print(f"     ⭐ Stars: {repo.get('stars', 'N/A')}")
        print(f"     🐞 Issues: {repo.get('issues', 'N/A')}")
        print(f"     🔗 URL: {repo.get('url', 'N/A')}\n")

    # Prompt user to follow repos
    to_follow = input("Enter numbers of repos to follow (comma-separated), or press Enter to skip: ").strip()

    if to_follow:
        try:
            indices = [int(x.strip()) - 1 for x in to_follow.split(",")]
            followed = [repos[i] for i in indices if 0 <= i < len(repos)]
            if followed:
                save_followed_repos(followed)
                print(f"\n✅ Saved {len(followed)} repo(s) to follow-up list.\n")
            else:
                print("\n⚠️ No valid selections made.\n")
        except ValueError:
            print("\n⚠️ Invalid input. Skipping follow-up step.\n")
