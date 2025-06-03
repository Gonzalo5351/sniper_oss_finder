# src/fetcher.py

import os
import requests

GITHUB_API_URL = "https://api.github.com"

class GitHubFetcher:
    def __init__(self, token=None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("Error: GitHub token not found. Configure the GITHUB_TOKEN environment variable.")
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json",
        }

    def search_repos_by_org(self, org_name, per_page=10):
        """Search for an organization's public repositories"""
        url = f"{GITHUB_API_URL}/orgs/{org_name}/repos"
        params = {"per_page": per_page, "sort": "updated"}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        return [
            {
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "updated_at": repo["updated_at"]
            }
            for repo in response.json()
        ]
