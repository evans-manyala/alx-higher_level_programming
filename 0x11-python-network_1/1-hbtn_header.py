#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
# Fetch the URL argument
    url = sys.argv[1]
    
    request = urllib.request.urlopen(url)
    with urllib.request.urlopen(url) as response:
        # Display the value
        print(dict(response.headers).get("X-Request-Id"))
