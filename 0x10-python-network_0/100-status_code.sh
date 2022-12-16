#!/bin/bash
# sends a request displays only the status code of the response.
curl -s -w "%{http_code}" "$1" -o /dev/null
