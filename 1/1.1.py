#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/1
By: Jimmy Chen
Date: 02/12/16
"""

import sys, re

f = open('1.txt', 'r')
steps = f.read().split(",")

pos = [0, 0]
positionsVisited = []

"""
0 = north
1 = east
2 = south
3 = west
"""
direction = 0

positionsVisited.append([pos[0], pos[1]])
for step in steps:
    # print("pos: " + str(pos))
    # print("visited: " + str(positionsVisited) + "\n")
    # print("visited: " + str(positionsVisited) + "\n")

    turnDirection = re.search('(L|R)', step).group(0)
    walkLength = int(re.search('\d+', step).group(0))
    # print("direction: %s, length: %s" % (turnDirection, walkLength))

    if turnDirection == 'L':
        direction -= 1
    elif turnDirection == 'R':
        direction += 1

    # wrap back around
    if direction > 3:
        direction -= 4
    elif direction < 0:
        direction += 4

    for i in range(0, walkLength):
        if direction == 0:
            pos[1] += 1
        elif direction == 1:
            pos[0] += 1
        elif direction == 2:
            pos[1] -= 1
        elif direction == 3:
            pos[0] -= 1

        if pos in positionsVisited:
            print("x: %d, y: %d" % (pos[0], pos[1]))
            print("%d blocks away" % (abs(pos[0]) + abs(pos[1])))
            sys.exit(0)
        positionsVisited.append([pos[0], pos[1]])
