#!/usr/bin/python3
""" a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username, password = sys.argv[1:]
    credentials = HTTPBasicAuth(username, password)
    api_url = f"https://api.github.com/user"
    resp = requests.get(api_url, auth=credentials)
    data = resp.json()
    print(data.get('id'))
