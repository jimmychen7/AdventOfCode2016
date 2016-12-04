"""
http://adventofcode.com/2016/day/3
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 04/12/16
"""
import re


def validTriangle(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)

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
lines = f.readlines()

for index, line in enumerate(lines):
    if index % 3 != 0:
        continue
    if index + 3 > len(lines):
        continue

    triLengths1 = re.findall('\d+', lines[index])
    triLengths2 = re.findall('\d+', lines[index + 1])
    triLengths3 = re.findall('\d+', lines[index + 2])

    if validTriangle(triLengths1[0], triLengths2[0], triLengths3[0]):
        numValidTriangles += 1
    if validTriangle(triLengths1[1], triLengths2[1], triLengths3[1]):
        numValidTriangles += 1
    if validTriangle(triLengths1[2], triLengths2[2], triLengths3[2]):
        numValidTriangles += 1

print("num valid triangles: %d" % numValidTriangles)
