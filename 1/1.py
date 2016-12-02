#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/1
By: Jimmy Chen
Date: 02/12/16
"""

import re

f = open('1.txt', 'r')
steps = f.read().split(",")

pos = {'x':0, 'y':0}

"""
0 = north
1 = east
2 = south
3 = west
"""
direction = 0

for step in steps:
    turnDirection = re.search('(L|R)', step).group(0)
    walkLength = int(re.search('\d+', step).group(0))
    # print("direction: %s, length: %s" % (turnDirection, walkLength))

    if turnDirection == 'L':
        direction -= 1
    else:
        direction += 1

    # wrap back around
    if direction > 3:
        direction -= 4
    elif direction < 0:
        direction += 4

    if direction == 0:
        pos['y'] += walkLength
    elif direction == 1:
        pos['x'] += walkLength
    elif direction == 2:
        pos['y'] -= walkLength
    elif direction == 3:
        pos['x'] -= walkLength


print("x: %d, y: %d" % (pos['x'], pos['y']))
print("%d blocks away" % (abs(pos['x']) + abs(pos['y'])))
