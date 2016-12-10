"""
http://adventofcode.com/2016/day/4
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 07/12/16
"""

import re

f = open('4.txt', 'r')

sum_sector_id = 0
for line in f:
    line.rstrip()
    sections = re.split('-', line)

    letter_count = {}
    for section in sections[:-1]:
        for letter in section:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    sorted_keys = []
    for key in sorted(letter_count, key=letter_count.get, reverse=True):
        sorted_keys.append(key)

    sector_id = re.search('\d+', sections[-1]).group(0)
    checksum = re.search('[^\d\[\]]+', sections[-1]).group(0)

    # rearrange sorted_keys so that keys that give equal
    # value are sorted alphabetically
    for index, key in enumerate(sorted_keys):
        if index < len(sorted_keys) - 1:
            if letter_count[key] == letter_count[sorted_keys[index + 1]]:
                if key > sorted_keys[index + 1]:
                    sorted_keys[index] = sorted_keys[index + 1]
                    sorted_keys[index + 1] = key

    # print("".join(sorted_keys[:5]))

    for index, letter in enumerate(checksum):
        if sorted_keys[index] != letter:
            break

    if index < 4:
        continue
    else:
        # real room
        decrypted_string = ""

        for section in sections[:-1]:
            for letter in section:
                decrypted_letter = (chr((
                                    ord(letter.lower()) +
                                    int(sector_id) % 26)))

                if decrypted_letter > 'z':
                    decrypted_letter = (chr(
                                        ord('a') +
                                        ord(decrypted_letter) -
                                        ord('z') - 1))

                decrypted_string += decrypted_letter
            decrypted_string += " "

        if re.search("object", decrypted_string):
            print("-".join(sections))
            print(decrypted_string)

