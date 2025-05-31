# src/analyzer.py
from datetime import datetime, timezone

POPULAR_LANGUAGES = {"Python", "JavaScript", "TypeScript", "Rust", "Go"}
KEYWORDS = {"framework", "tool", "automation", "data", "api"}

class RepositoryAnalyzer:
    def __init__(self, repos):
        self.repos = repos

    def score_repo(self, repo):
        score = 0

        # 1. Stars
        stars = repo.get("stargazers_count", 0)
        score += min(stars // 100, 10)  # Máximum +10 per stars

        # 2. Last update 
        updated_at = repo.get("updated_at")
        if updated_at:
            updated_date = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            days_since_update = (datetime.now(timezone.utc) - updated_date).days
            if days_since_update < 30:
                score += 5
            elif days_since_update < 90:
                score += 3
            elif days_since_update < 180:
                score += 1

        # 3. Popular language
        if repo.get("language") in POPULAR_LANGUAGES:
            score += 2

        # 4. Key words in the description
        description = repo.get("description") or ""
        if any(keyword in description.lower() for keyword in KEYWORDS):
            score += 2
        
        return score

    def analyze(self):
        analyzed = []
        for repo in self.repos:
            repo_score = self.score_repo(repo)
            repo["score"] = repo_score
            analyzed.append(repo)
        
        # Orden descendente por score
        return sorted(analyzed, key=lambda r: r["score"], reverse=True)



