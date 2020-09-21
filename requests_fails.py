import json
import requests

with open("./token.json", "r") as f:
    auth_token = json.load(f)["token"]

headers = {"Authorization": "token {}".format(auth_token)}
url = "https://api.github.com/repos/seanbreckenridge/albums/traffic/clones"

# this fails, for some reason, even though the corresponding curl works fine
r = requests.get(url, headers=headers)
print(r.json())
r.raise_for_status()
