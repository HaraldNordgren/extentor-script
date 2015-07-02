#!/usr/bin/python

import requests
import httplib

URL_START = "http://www.maths.lth.se/na/courses/FMN011/media/material/pract150522"
WILDCARDS = ["", "_", "__", "___", "_1", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]

def http_request(url):
    r = requests.get(url)
    if (r.status_code == httplib.OK):
        print("  " + url)

for wildcard in WILDCARDS:
    url = URL_START + wildcard + ".pdf"
    http_request(url)
