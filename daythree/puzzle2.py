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
import re

grid = [[]]
widest = 0
highest = 0
claimArr = []
for items in data.splitlines():
    claim = [int(s) for s in re.findall(r'\d+', items)]
    claim.append(0)

    claimArr.append(claim)
    #[1, 808, 550, 12, 22]
    #[id,  x,   y, xl, yl]
    width = claim[3] + claim[1]
    height = claim[4] + claim[2]

    if width > widest:
        for x in range(widest, width):
            grid.append([])
            for y in range(highest):
                grid[x + 1].append(0)
        widest = width

    if height > highest:
        for x in grid:
            if len(x) <= height:
                for y in range(height - highest):
                    x.append(0)
        highest = height



    for x in range(claim[3]):
        xx = x + claim[1]
        for y in range(claim[4]):
            yy = y + claim[2]

            if grid[xx][yy] == 0:
                grid[xx][yy] = claim[0]
            else:
                gridclaim = grid[xx][yy] - 1
                thisclaim = claim[0] - 1

                claimArr[gridclaim][5] = 1
                claimArr[thisclaim][5] = 1

for claim in claimArr:
    if claim[5] == 0: 
        print(claim[0])



