#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the value
 of the variable X-Request-Id in the response header

 Requirements:
 - You must use the packages requests and sys
 - You are not allow to import other packages than requests and sys
 - The value of this variable is different for each request
 - You don’t need to check script arguments (number and type)
"""
import requests
from sys import argv


def main():
    """Read Header"""
    url = argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
