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
index = 482658
password = ""
m = hashlib.md5()

hash_key = door_id + str(index)
print(hash_key)
m.update("%s" % (hash_key))
hash_value = m.hexdigest()
print("\n\nindex = %s, hash = %s, password = %s" % (index,
                                                            hash_value,
                                                            password))
