import requests
import httplib

URL_START = "http://www.maths.lth.se/na/courses/FMN011/media/material/exam"
WILDCARDS = ["", "_", "__", "___", "_1", "_2"] #, "_3", "_4", "_5", "_6", "_7", "_8", "_9"]
SOLUTION = ["", "sol"]

EXAM_DATES = ["070528", "110603", "120528", "130603", "140602"]
#EXAM_DATES = ["140822", "140113", "130823", "130114", "120824", "120112"]

def dates_small():
    dates = []
    for y in range(0,16):
        year = str(y).zfill(2)
        for x in range(20,32):
            dates.append(year + "05" + str(x).zfill(2))
        for x in range(1,11):
            dates.append(year + "06" + str(x).zfill(2))
    return dates

def http_request(url):
    r = requests.get(url)
    if (r.status_code == httplib.OK):
        print("  " + url)

def find_exams(date):
    for solution in SOLUTION:
        for wildcard in WILDCARDS:
            url = URL_START + date + solution + wildcard + ".pdf"
            http_request(url)

def all_dates():
    dates = []
    for y in range(0,16):
        year = str(y).zfill(2)
        for m in range(1,13):
            month = str(m).zfill(2)
            for d in range(1,32):
                day = str(d).zfill(2)
                dates.append(year + month + day)

    return dates

for date in dates_small():
    print(date + ":")
    find_exams(date)

# All dates:
# 5952 * 13 * 2 = 154752 requests
# 154752 / 70 = 2211 seconds = 
 
# 5 * 13 * 2 = 130 requests
