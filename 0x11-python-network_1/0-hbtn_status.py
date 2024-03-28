#!/usr/bin/python3
"""0. What's my status? #0"""

import urllib.request


if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as response:
        data = response.read()
        utf_data = data.decode('utf-8')
        resType = type(data)
        print(f"Body response:\n\t- type: {resType}\n\t- \
content: {data}\n\t- utf8 content: {utf_data}")
