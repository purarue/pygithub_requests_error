#!/bin/bash

token="$(jq -r '.token' <./token.json)"
# a repo I have push access to (the first one returned by get_repos())
url='https://api.github.com/repos/abhinavk99/jikanpy/traffic/views'
# this fails (as it should)
curl -vs "$url" 2>&1
# this succeeds
curl -vs -H "Authorization: token $token" "$url" 2>&1
