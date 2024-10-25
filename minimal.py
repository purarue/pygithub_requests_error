#!/usr/bin/env python3

import json
from typing import Callable, Any

import requests
import httpx


# extract status/status_code from the requests/httpx item
def extract_status(obj: Any) -> int:
    if hasattr(obj, "status"):
        return obj.status
    if hasattr(obj, "status_code"):
        return obj.status_code
    raise TypeError("unsupported request object")


def make_request(using_verb: Callable[..., Any], url: str, headers: Any) -> Any:
    print("using", using_verb, url)
    resp = using_verb(url, headers=headers)

    status = extract_status(resp)

    print(str(repr(resp.json())))
    if status == 200:
        print("succeeded")
        return resp
    else:
        print("failed")
        resp.raise_for_status()

def main():
    # see https://github.com/purarue/pygithub_requests_error for token scopes
    with open("./token.json", "r") as f:
        auth_token = json.load(f)["token"]

    headers = {"Authorization": "token {}".format(auth_token), "User-Agent": "requeststest"}

    # replace this with a URL you have access to
    url = "https://api.github.com/repos/purarue/albums/traffic/clones"

    make_request(httpx.get, url, headers)
    make_request(requests.get, url, headers)

if __name__ == "__main__":
    main()
