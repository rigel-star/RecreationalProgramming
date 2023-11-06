#!/usr/bin/env python3

import q1
pos = 0
floor = 0
for i in q1.inp:
    pos += 1
    floor += 1 if i == "(" else -1
    if floor == -1: break

print(pos)
