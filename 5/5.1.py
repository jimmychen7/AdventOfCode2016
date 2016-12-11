#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/5
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 11/12/16
"""

import sys
import hashlib
import re

if len(sys.argv) != 2:
    sys.stderr.write("Usage: %s <Door ID>" % sys.argv[0])
    sys.exit(1)

door_id = sys.argv[1]
index = 0
password = ['#'] * 8
positions_filled = []

while '#' in password:
    hash_key = door_id + str(index)
    m = hashlib.md5()
    m.update(b"%s" % hash_key)
    hash_value = m.hexdigest()

    if re.match('00000', hash_value) and re.match('^\d$', hash_value[5]):
        if (int(hash_value[5]) < 8 and int(hash_value[5]) >= 0 and
                int(hash_value[5]) not in positions_filled):
            password[int(hash_value[5])] = hash_value[6]
            positions_filled.append(int(hash_value[5]))
            print("\n\nindex = %s, hash = %s, password = %s" % (index,
                                                                hash_value,
                                                                password))
    index += 1

print("\n\npassword = %s" % "".join(password))
