#!usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
Using the package requests to display reponse in tabulation before -
"""

import requests


if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))