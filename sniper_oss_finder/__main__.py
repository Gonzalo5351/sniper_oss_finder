# src/__main__.py

import typer
from sniper_oss_finder.fetcher import GitHubFetcher
from sniper_oss_finder.analyzer import RepositoryAnalyzer
from sniper_oss_finder.reporter import display_report
from sniper_oss_finder.persister import save_followed_repos

app = typer.Typer()

@app.command()
def run(org: str = typer.Option(..., help="GitHub organization name"),
        per_page: int = typer.Option(10, help="Repos per page to fetch"),
        follow_top: int = typer.Option(0, help="Auto-follow top N repos")):
    """
    Fetch, analyze and optionally auto-follow repos from a GitHub organization.
    """
    try:
        fetcher = GitHubFetcher()
        repos = fetcher.search_repos_by_org(org, per_page=per_page)

        analyzer = RepositoryAnalyzer(repos)
        ranked_repos = analyzer.analyze()

        display_report(ranked_repos, interactive=(follow_top == 0))

        if follow_top > 0:
            top_repos = ranked_repos[:follow_top]
            save_followed_repos(top_repos)
            typer.echo(f"\n✅ Auto-followed top {follow_top} repo(s).\n")

    except Exception as e:
        typer.echo(f"❌ Error: {e}")

if __name__ == "__main__":
    app()
