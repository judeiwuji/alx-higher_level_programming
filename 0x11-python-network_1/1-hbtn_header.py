#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.

Requirements:
    - You must use the packages urllib and sys
    - You are not allow to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
    - You must use a with statement
"""
from urllib.request import Request
from urllib.request import urlopen
from sys import argv


def main():
    """Read header content"""
    url = argv[1]
    req = Request(url)
    with urlopen(req) as res:
        content = res.info().get("x-request-id")
        print(content)


if __name__ == "__main__":
    main()
