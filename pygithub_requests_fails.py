import json

from github import Github, enable_console_debug_logging

enable_console_debug_logging()

with open("./token.json", "r") as f:
    auth_token = json.load(f)["token"]

g = Github(auth_token)

repo = next(iter(g.get_user().get_repos()))
# this fails with a 403
print(repo.get_views_traffic())
