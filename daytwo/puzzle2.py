#!/usr/bin/python3
import sys
import urllib.request
import urllib.error

#pass in 1st argument as url to pull data from
#pass in 2nd argument as string to pass into cookie session variable
url = sys.argv[1]
session = sys.argv[2]
header = {'Cookie':'session=' + session}
req = urllib.request.Request(url, None, header)

try: 
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('failed: ', e.reason)
    elif hasattr(e, 'code'):
        print('conldnt fulfill request: ', e.code)
else:
    with response as d:
        data = d.read().decode('utf-8')



#data variable is data from website
idlist = data.splitlines()

for currid in idlist:
    bestmatch = ''
    for compid in idlist: 
        if compid != currid:
            matched = ''
            index = 0
            for letter in currid:
                if letter == compid[index]:
                    matched += letter
                index += 1
            if len(bestmatch) < len(matched):
                bestmatch = matched

    if len(bestmatch)> 24:
        print(bestmatch)




