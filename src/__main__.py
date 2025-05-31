# src/main.py

from fetcher import GitHubFetcher
from analyzer import RepositoryAnalyzer

fetcher = GitHubFetcher()
repos = fetcher.search_repos_by_org("pallets")  # Example with a org of Flask

analyzer = RepositoryAnalyzer(repos)
ranked_repos = analyzer.analyze()

for repo in ranked_repos:
    print(f"{repo['name']} ({repo['score']} pts) - {repo['url']}")
