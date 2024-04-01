#!/usr/bin/python3

"""
Python script checks a users githib repository
name and owner name then displays the commits
of the repository
"""

import sys
import requests

if __name__ == "__main__":
    repoName = sys.argv[1]
    repoOwner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        repoOwner,
        repoName)

    request = requests.get(url)
    commits = request.json()
    try:
        for _ in range(10):
            print("{}: {}".format(
                commits[_].get("sha"),
                commits[_].get("commit").get("author").get("name")))
    except IndexError:
        pass
