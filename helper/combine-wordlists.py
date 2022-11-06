#!/usr/bin/env python

import sys
import itertools

lists = []
for filename in sys.argv[1:]:
    words = []
    with open(filename) as fp:
        for line in fp:
            words.append(line.rstrip())
    lists.append(words)

for element in itertools.product(*lists):
    print("".join(element))
