#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 15/12/16
"""

import re


def supports_tls(line):
    substrings = re.findall('[^\[\]]+', line)
    hypernet_sequences = re.findall('\[\w*\]', line)

    for hypernet_sequence in hypernet_sequences:
        if has_abba(hypernet_sequence):
            return False

    for substring in substrings:
        if has_abba(substring):
            return True


def has_abba(string):
    for index in range(0, len(string) - 3):
        substring = string[index:index + 4]
        if substring[0] == substring[1]:
            continue
        elif substring[0] == substring[3] and substring[1] == substring[2]:
            return True
        else:
            continue
    return False


num_ips = 0
f = open('7.txt', 'r')
for line in f:
    ip_addr = line.rstrip()
    if supports_tls(ip_addr):
        num_ips += 1

print("num IPs that support TLS: %s" % num_ips)
