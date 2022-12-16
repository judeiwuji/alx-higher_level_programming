#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response.

Requirements:
 - If the HTTP status code is greater than or equal to 400, print:
   Error code: followed by the value of the HTTP status code
 - You must use the packages requests and sys
 - You are not allowed to import packages other than requests and sys
 - You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv


def main():
    """Read Header"""
    url = argv[1]
    res = requests.get(url)
    errorCode = res.status_code
    if errorCode < 400:
        print(res.text)
    else:
        print("Error code: {}".format(errorCode))



if __name__ == "__main__":
    main()
