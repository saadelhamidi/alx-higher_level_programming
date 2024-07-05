#!/usr/bin/python3
"""  a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    code = req.status_code
    if code == 200:
        print(req.text)
    else:
        print("Error code:", code)
