#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        print("No results")
    else:
        response = requests.post(url, data={'q': sys.argv[1]})
        try:
            json_r = response.json()

            if json_r:
                print("[{}] {}".format(json_r.get('id'), json_r.get('name')))
            else:
                print("No results")
        except ValueError:
            print("Not a valid JSON")
