#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write(f"Usage: {sys.argv[0]} <URL>\n")
        sys.exit(1)
        
        # Complete the URL from the command line argument
        url = sys.argv[1]
        
        # Complete a GET request to the URL
        response = requests.get(url)
        print(response.headers.get("X-Request-Id"))
