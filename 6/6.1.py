#!/usr/bin/env python

"""
http://adventofcode.com/2016/day/6
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 15/12/16
"""
import operator
import sys

f = open('6.txt', 'r')
lines = f.readlines()
count = []

for letter in lines[0].rstrip():
    count.append({})

for line in lines:
    line = line.rstrip()
    for col, letter in enumerate(line):
        if letter in count[col]:
            count[col][letter] += 1
        else:
            count[col][letter] = 1

for letter_count in count:
    sorted_count = sorted(letter_count.items(), key=operator.itemgetter(1))
    # sorted_count.reverse()
    sys.stdout.write(sorted_count[0][0])
