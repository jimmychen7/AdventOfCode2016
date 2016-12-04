"""
http://adventofcode.com/2016/day/3
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 04/12/16
"""
import re


def validTriangle(triangleLengths):
    a = int(triangleLengths[0])
    b = int(triangleLengths[1])
    c = int(triangleLengths[2])

    if a + b > c:
        if a + c > b:
            if b + c > a:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


numValidTriangles = 0
f = open('3.txt', 'r')
for line in f:
    triangleLengths = re.findall('\d+', line)
    if validTriangle(triangleLengths):
        numValidTriangles += 1

print("num valid triangles: %d" % numValidTriangles)
