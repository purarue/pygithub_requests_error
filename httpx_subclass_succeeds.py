import json

import httpx
from github.Requester import RequestsResponse, HTTPSRequestsConnectionClass, Requester

# store header info to make sure that requests are actually working
GLOBAL_HEADERS = {}

# subclass to use httpx instead of requests
class HttpxConnectionClass(HTTPSRequestsConnectionClass):

    # store request header info for each request, to show that we're actually using the rate limit
    def storeinfo(self, request_headers, response):
        response_info = {}
        for key, val in response.headers.items():
            response_info[key] = val
        GLOBAL_HEADERS[self.url] = {
            "request": request_headers,
            "response": response_info,
        }

    # overwrite the HTTPSRequestsConnectionClass getresponse function
    def getresponse(self):
        verb = getattr(httpx, self.verb.lower())
        url = "%s://%s:%s%s" % (self.protocol, self.host, self.port, self.url)
        if self.verb.lower() == "get":
            r = verb(url, headers=self.headers)
        else:  # for post requests
            r = verb(
                url,
                headers=self.headers,
                data=self.input,
            )
        self.storeinfo(self.headers, r)
        return RequestsResponse(r)


Requester._Requester__httpsConnectionClass = HttpxConnectionClass

with open("./token.json", "r") as f:
    auth_token = json.load(f)["token"]

from github import Github, enable_console_debug_logging

enable_console_debug_logging()

g = Github(auth_token)

repo = next(iter(g.get_user().get_repos()))
print(repo.get_views_traffic())

# store request/response headers
with open("httpx_headers.txt", "w") as f:
    json.dump(GLOBAL_HEADERS, f)
