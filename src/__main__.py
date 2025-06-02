# src/main.py

from fetcher import GitHubFetcher
from analyzer import RepositoryAnalyzer
from reporter import display_report

fetcher = GitHubFetcher()
repos = fetcher.search_repos_by_org("pallets")  # Example with a org of Flask

analyzer = RepositoryAnalyzer(repos)
ranked_repos = analyzer.analyze()

display_report(ranked_repos)


