#!/usr/bin/python2

import requests, httplib, time

#URL_START = "http://www.ctr.maths.lu.se/media/exams/opt/exam_2015-05-07.pdf"
URL_START = "http://www.ctr.maths.lu.se/media/exams/opt/"

def dates_small():
    dates = []
    
    #for y in range(9,8,-1):
    for y in range(15,9,-1):
        year = "20" + str(y).zfill(2) + "-"

        # Test all
        """
        for m in range(1, 13):
            for x in range(1, 32):
                dates.append(year + str(m).zfill(2) + "-" + str(x).zfill(2))
        """

        for x in range(20,32):
            dates.append(year + "08-" + str(x).zfill(2))
        for x in range(1,32):
            dates.append(year + "04-" + str(x).zfill(2))
        for x in range(13,23):
            dates.append(year + "12-" + str(x).zfill(2))

    return dates

def http_request(date, myfile):
    url = URL_START + "exam_" + date + ".pdf"
    r = requests.get(url)
    if (r.status_code == httplib.OK):
        print("  " + url)
        myfile.write(url + "\n")

        sol_url = URL_START + "solution_" + date + ".pdf"
        myfile.write(sol_url + "\n\n")

def find_exams(date, myfile):
    #print url
    http_request(date, myfile)
    time.sleep(0.1)

with open("exams.txt", "a") as myfile:

    for date in dates_small():
        print(date + ":")
        find_exams(date, myfile)