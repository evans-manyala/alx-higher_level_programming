#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

# Fetch the URL argument
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
   # Retrieve the response headers as a dictionary
   headers = response.info()

   # Extract the X-Request-Id value, handling potential errors
   x_request_id = headers.get('X-Request-Id', 'Not Found')

   # Display the value
   print(f"X-Request-Id: {x_request_id}")
