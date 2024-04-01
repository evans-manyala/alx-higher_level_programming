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
        username = sys.argv[1]
        credentials = sys.argv[2]
        verify = HTTPBasicAuth(username, credentials)
        feedback = requests.get("https://api.github.com/user", auth=verify)
        print(feedback.json("id"))
