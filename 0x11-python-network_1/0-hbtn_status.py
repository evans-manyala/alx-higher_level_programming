#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status
using urllib.
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status from the given URL
    and displays the body of the response.

    Args:
        url (str): The URL to fetch the status from.
    """

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    # Print the response body with tabs before each line
    print("\t".join(body.splitlines()))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)  # Call the function to fetch and display
