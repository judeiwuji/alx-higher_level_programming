#!/usr/bin/python3
"""
 Takes in a URL, sends a request to the URL and displays the
 body of the response (decoded in utf-8).

 Requirements:
 - You have to manage urllib.error.HTTPError exceptions and print: Error code:
   followed by the - HTTP status code
 - You must use the packages urllib and sys
 - You are not allowed to import other packages than urllib and sys
 - You don’t need to check arguments passed to the script (number or type)
 - You must use the with statement
"""

from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


def main():
    """Handle HttpError"""
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as res:
            content = res.read().decode("utf-8")
            print("{}".format(content))
    except HTTPError as error:
        print("Error code: {:d}".format(error.code))


if __name__ == "__main__":
    main()
