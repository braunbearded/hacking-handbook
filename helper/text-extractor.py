#!/usr/bin/env python

import sys
import os
import re
import collections

min_length = 4
max_length = 30
blacklist_reg = r"(x20[a-zA-Z0-9])"

file = sys.argv[1:][0]
if not os.path.isfile(file):
    print(f"{file} does not exists")
    exit()

lines = open(file).read().splitlines()

result = collections.defaultdict(int)
for line in lines:
    strings = "".join(re.findall(f"[^\x00-\x1F\x7F-\xFF]{{{min_length},}}", line))
    result[strings] += 1
    # reg_str = re.findall("<[a-zA-z ]>(.*?)</[a-zA-Z ]>", strings)
    tokens = re.findall("\w+", line)
    for token in tokens:
        if not re.match(blacklist_reg, token.strip()):
            result[token.strip()] += 1

result = {
    k: v for k, v in result.items() if len(k) >= min_length and len(k) <= max_length
}
result = sorted(result.items(), key=lambda item: item[1] - len(item[0]), reverse=True)

for k, v in result:
    print(f"{v:<5} {k}")
