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
overlap = 0
for items in data.splitlines():
    itemArr = [int(s) for s in re.findall(r'\d+', items)]
    #[1, 808, 550, 12, 22]
    #[id,  x,   y, xl, yl]
    width = itemArr[3] + itemArr[1]
    height = itemArr[4] + itemArr[2]

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



    for x in range(itemArr[3]):
        xx = x + itemArr[1]
        for y in range(itemArr[4]):
            yy = y + itemArr[2]
            grid[xx][yy] += 1
            if grid[xx][yy] == 2:
                overlap += 1

print(overlap)



