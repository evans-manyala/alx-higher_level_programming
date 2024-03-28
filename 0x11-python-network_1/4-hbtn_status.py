#!usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
Using the package requests to display reponse in tabulation before -
"""

import urllib.request

if __name__ == "__main__":

    # Define the URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
    print("\t- utf8 content: {}".format(response.text.encode("utf-8")))
