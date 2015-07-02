#!/usr/bin/python

import requests
import httplib

#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-01.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-02.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-03.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-04.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-05.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-06_2.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-07.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-08.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-09.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-10.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-11.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-13_2.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-14_3.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-15_2.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-15-15.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-14-16.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-13-18.pdf
#http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-14-18.pdf

URL_START = "http://www.maths.lth.se/na/courses/FMN011/media/material/fmn011-"
WILDCARDS = ["", "_2", "_3"]

def lectures():
    lec = []
    for x in range(0,21):
        lec.append( str(x).zfill(2) )
    return lec

def http_request(url):
    r = requests.get(url)
    if (r.status_code == httplib.OK):
        print("  " + url)

for lec in lectures():
    print lec + ":"
    for y in range(13,16):
        for w in WILDCARDS:
            url = URL_START + str(y) + "-" + lec + w + ".pdf"
            http_request(url)
