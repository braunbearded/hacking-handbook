#!/usr/bin/env python

import sys
import re
import collections
from pathlib import Path

min_length = 4
max_length = 30
blacklist_reg = r"(x20[a-zA-Z0-9]|\[[\\\|\-/]\] Working on it\.\.\.|[94m[*])"

if len(sys.argv) < 2:
    print(f"Usage: txe <file.txt/regex>")
    exit(1)

debug = True
if len(sys.argv) == 3:
    debug = False

result = collections.defaultdict(int)

regex = sys.argv[1:][0]

# print(f"Using the following regex: {regex}")
files = Path(".").rglob(regex)

for file in files:

    lines = open(file).read().splitlines()

    for line in lines:
        strings = "".join(re.findall(f"[^\x00-\x1F\x7F-\xFF]{{{min_length},}}", line))
        if not re.match(blacklist_reg, strings):
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

out = ""

if debug:
    for k, v in result:
        out += f"{v:<5} {k}\n"
else:
    for k, v in result:
        out += f"{k}\n"

print(out)
