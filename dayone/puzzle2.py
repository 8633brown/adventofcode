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
opList = []
freqList = []
currFreq = 0
opIndex = 0

for line in data.splitlines():
    op = int(line)
    opList.append(op)
    freqList.append(currFreq)
    currFreq += op
    if currFreq in freqList:
        print(currFreq)

while currFreq not in freqList:

    freqList.append(currFreq)
    currFreq += opList[opIndex]

    opIndex += 1
    if opIndex == len(opList):
        opIndex = 0

print(currFreq)
