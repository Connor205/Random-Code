import os
import requests
from pprint import pprint

token = os.environ["GITHUB_TOKEN0"]
baseUrl = 'https://api.github.com/users/connor205'
repoUrl = baseUrl + "/repos"

github = requests.Session()

github.auth = ("connor205", token)

repos = github.get(repoUrl).json()
pprint(repos)
for repo in repos:
    print(repo["url"])