"""
http://adventofcode.com/2016/day/2
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 04/12/16
"""

f = open('2.txt', 'r')

pos = {'x': 1, 'y': 1}
code = ""

for line in f:
    key = "?"
    for letter in line:

        if letter == 'U':
            pos['y'] -= 1
        elif letter == 'D':
            pos['y'] += 1
        elif letter == 'L':
            pos['x'] -= 1
        elif letter == 'R':
            pos['x'] += 1

        # stay within kaypad boundary
        if pos['x'] < 0:
            pos['x'] = 0
        elif pos['x'] > 2:
            pos['x'] = 2

        if pos['y'] < 0:
            pos['y'] = 0
        elif pos['y'] > 2:
            pos['y'] = 2

    # determine key pressed
    if pos['y'] == 0:

        if pos['x'] == 0:
            key = '1'
        elif pos['x'] == 1:
            key = '2'
        elif pos['x'] == 2:
            key = '3'

    elif pos['y'] == 1:

        if pos['x'] == 0:
            key = '4'
        elif pos['x'] == 1:
            key = '5'
        elif pos['x'] == 2:
            key = '6'

    elif pos['y'] == 2:

        if pos['x'] == 0:
            key = '7'
        elif pos['x'] == 1:
            key = '8'
        elif pos['x'] == 2:
            key = '9'

    code += key

print(code)