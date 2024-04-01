#!/usr/bin/python3
"""
Python script using basic authentication is able 
to use GitHub Credentials and GitHub APIs to print
UserID
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if "___name__" == "__main__":
        url = "https://api.github.com/user"
        verify = HTTPBasicAuth(sys.argv[1], sys.argv[2])
        response = requests.get(url, auth=verify)
        print(response.json().get("id"))
