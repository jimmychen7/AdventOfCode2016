"""
http://adventofcode.com/2016/day/2
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 04/12/16
"""


# width is the number of number from the middle exclusive
def limitPos(number, width):
    if number > 2 + width:
        return 2 + width

    elif number < 2 - width:
        return 2 - width

    else:
        return number


f = open('2.txt', 'r')
pos = {'x': 0, 'y': 2}
code = ""

for line in f:
    key = "?"
    for letter in line:

        if letter == 'U':

            pos['y'] -= 1
            if pos['x'] < 2:
                pos['y'] = limitPos(pos['y'], pos['x'])
            else:
                pos['y'] = limitPos(pos['y'], 4 - pos['x'])

        elif letter == 'D':

            pos['y'] += 1
            if pos['x'] < 2:
                pos['y'] = limitPos(pos['y'], pos['x'])
            else:
                pos['y'] = limitPos(pos['y'], 4 - pos['x'])

        elif letter == 'L':

            pos['x'] -= 1
            if pos['y'] < 2:
                pos['x'] = limitPos(pos['x'], pos['y'])
            else:
                pos['x'] = limitPos(pos['x'], 4 - pos['y'])

        elif letter == 'R':

            pos['x'] += 1
            if pos['y'] < 2:
                pos['x'] = limitPos(pos['x'], pos['y'])
            else:
                pos['x'] = limitPos(pos['x'], 4 - pos['y'])

    # determine key pressed
    if pos['y'] == 0:

        key = '1'

    elif pos['y'] == 1:

        if pos['x'] == 1:
            key = '2'
        elif pos['x'] == 2:
            key = '3'
        elif pos['x'] == 3:
            key = '4'

    elif pos['y'] == 2:

        if pos['x'] == 0:
            key = '5'
        elif pos['x'] == 1:
            key = '6'
        elif pos['x'] == 2:
            key = '7'
        elif pos['x'] == 3:
            key = '8'
        elif pos['x'] == 4:
            key = '9'

    elif pos['y'] == 3:

        if pos['x'] == 1:
            key = 'A'
        elif pos['x'] == 2:
            key = 'B'
        elif pos['x'] == 3:
            key = 'C'

    elif pos['y'] == 4:

        key = 'D'

    code += key

print(code)