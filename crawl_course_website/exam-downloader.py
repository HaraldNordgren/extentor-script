#!/usr/bin/env python3


import sys, os, urllib

from bs4 import BeautifulSoup


url             = sys.argv[1]
directory       = sys.argv[2]

content         = urllib.request.urlopen(url).read()
soup            = BeautifulSoup(content, 'html.parser')

table = soup.find('table', attrs={'class':'contenttable'})

for table_entry in table.tbody.find_all('tr'):
    for a in table_entry.td.find_all('a'):
        
        link = a['href']
        filename = directory + '/' + os.path.basename(link)
        
        urllib.request.urlretrieve(link, filename)
