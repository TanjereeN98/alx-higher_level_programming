#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    result = r.headers.get('X-Request-Id')
    print(result)
