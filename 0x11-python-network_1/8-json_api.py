#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": q})

    try:
        json_r = response.json()

        if json_r:
            print(f"[{json_r.get('id')}]{json_r.get('name')}")
        else:
            print("No results")
    except ValueError:
        print("Not a valid JSON")
