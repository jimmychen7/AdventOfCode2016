"""
http://adventofcode.com/2016/day/4
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 07/12/16
"""

import re, operator

f = open('4.txt', 'r')

sum_sector_id = 0
for line in f:
    line.rstrip()
    sections = re.split('-', line)
    #print(sections)
    
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
    
    #rearrange sorted_keys so that keys that give equal value is sorted alphabetically
    for index, key in enumerate(sorted_keys):
        if index < len(sorted_keys)-1:
            if letter_count[key] == letter_count[sorted_keys[index+1]]:
                if key > sorted_keys[index+1]:
                    sorted_keys[index] = sorted_keys[index+1]
                    sorted_keys[index+1] = key
    
    print("".join(sorted_keys[:5])) 
            
    for index, letter in enumerate(checksum):
        if sorted_keys[index] != letter:            
            break

    if index < 4:
        print("%s %s %s\n" % (checksum, sector_id, sum_sector_id))
        continue
    else:
        sum_sector_id += int(sector_id)
        print("%s %s %s ############ real #############\n" % (checksum, sector_id, sum_sector_id))

print(sum_sector_id)
        
    
            


