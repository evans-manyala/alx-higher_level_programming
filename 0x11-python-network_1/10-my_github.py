#!/usr/bin/python3
"""Python script using basic authentication is able
to use GitHub Credentials and GitHub APIs to print
UserID"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
