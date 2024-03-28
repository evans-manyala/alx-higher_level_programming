#!usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
Using the package requests to display reponse in tabulation before -
"""

import requests

if __name__ == "__main__":

    # Define the URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Display the body of the response in the desired format
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    else:
        # Print an error message if the request was not successful
        print(f"Error fetching URL. Status code: {response.status_code}")
