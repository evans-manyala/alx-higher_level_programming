#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the
response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get URL and email
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email parameter
    params = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request  to the url with email
    with urllib.request.urlopen(url, data=params) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
