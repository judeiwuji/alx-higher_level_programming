#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)

Requirements:
 - The email must be sent in the email variable
 - You must use the packages urllib and sys
 - You are not allowed to import packages other than urllib and sys
 - You don’t need to check arguments passed to the script (number or type)
 - You must use the with statement
"""

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


def main():
    """Read header content"""
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = urlencode(values)
    data = data.encode("ascii")
    req = Request(url, data)

    with urlopen(req) as res:
        content = res.read().decode("utf-8")
        print("{}".format(content))


if __name__ == "__main__":
    main()
