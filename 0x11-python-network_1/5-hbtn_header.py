#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Check if the 'X-Request-Id' header is present in the response

        if "X-Request-Id" in response.headers:
            # Display the value of the 'X-Request-Id' header
            print("X-Request-Id:", response.headers["X-Request-Id"])
        else:
            print("X-Request-Id header not found in the response")
    else:
        # Print an error message if the request was not successful
        print(f"Error fetching URL. Status code: {response.status_code}")
