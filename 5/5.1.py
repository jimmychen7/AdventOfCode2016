#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 11/12/16
"""

import sys
import hashlib
import re
import time

if len(sys.argv) != 2:
    sys.stderr.write("Usage: %s <Door ID>" % sys.argv[0])
    sys.exit(1)

door_id = sys.argv[1]
index = 0
password = ""

while len(password) != 8:
    hash_key = door_id + str(index)
    m = hashlib.md5()
    m.update(b"%s" % hash_key)
    hash_value = m.hexdigest()
    # sys.stdout.write("%s: %s\n" % (index, hash_value))
    if re.match('00000', hash_value):
        password += hash_value[5]
        print("\n\nindex = %s, hash = %s, password = %s" % (index,
                                                            hash_value,
                                                            password))
    index += 1

print("\n\npassword = %s" % password)
