#!/usr/bin/python3
""" a Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repName, ownername = sys.argv[1:]
    credentials = HTTPBasicAuth(repName, ownername)
    api_url = f"https://api.github.com/repos/{ownername}/{repName}/commits"
    resp = requests.get(api_url)
    cm = resp.json()
    try:
        for i in range(10):
            print(f'{cm[i].get("sha")}: \
{cm[i].get("commit").get("author").get("name")}')
    except IndexError:
        pass
