#!/usr/bin/env python
"""
http://adventofcode.com/2016/day/7
By: Jimmy Chen (https://github.com/jimmychen7)
Date: 15/12/16
"""

import re


# string matches aba pattern
def is_aba(string):
    if string[0] != string[2]:
        return False
    if string[0] == string[1]:
        return False
    return True


def supports_ssl(line):
    substrings = re.findall('([^\[\]]+\[|\][^\[\]]+)', line)
    hypernet_sequences = re.findall('\[\w*\]', line)
    bab_sequences = []
    for hypernet_sequence in hypernet_sequences:
        for index in range(0, len(hypernet_sequence) - 2):
            substring = hypernet_sequence[index:index + 3]
            if not is_aba(substring):
                continue
            bab_sequences.append(substring)

    for substring in substrings:
        substring = re.sub('(\[|\])', '', substring)
        for index in range(0, len(substring) - 2):
            string_sequence = substring[index:index + 3]
            if not is_aba(string_sequence):
                continue
            aba_sequence = string_sequence
            bab_sequence = aba_sequence[1] + aba_sequence[0] + aba_sequence[1]
            if bab_sequence in bab_sequences:
                return True

    return False


num_ips = 0
f = open('7.txt', 'r')
for line in f:
    ip_addr = line.rstrip()
    if supports_ssl(ip_addr):
        num_ips += 1

print("num IPs that support SSL: %s" % num_ips)
