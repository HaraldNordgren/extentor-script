#!/usr/bin/python

import requests
import httplib

URL_START = "http://fileadmin.cs.lth.se/cs/Education/"
COURSES = ["EDA050/", "EDAF35/"]

def dates_small():
    dates = []
    for y in range(0,17):
        year = "20" + str(y).zfill(2)
        for x in range(20,32):
            dates.append(year + "05" + str(x).zfill(2))
        for x in range(1,11):
            dates.append(year + "06" + str(x).zfill(2))
        for x in range(20,32):
            dates.append(year + "08" + str(x).zfill(2))
        for x in range(1,11):
            dates.append(year + "09" + str(x).zfill(2))
    return dates

def http_request(url):
    r = requests.get(url)
    if (r.status_code == httplib.OK):
        print("  " + url)

def find_exams(date):
    for course in COURSES:
        url = URL_START + course + date + ".pdf"
        http_request(url)

for date in dates_small():
    print(date + ":")
    find_exams(date)
