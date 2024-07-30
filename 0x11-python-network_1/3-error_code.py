#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            resp_content = resp.read().decode("utf-8")
            print(resp_content)
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
