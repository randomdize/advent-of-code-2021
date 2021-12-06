#!/usr/bin/env python3
import sys

filename = "input"

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    inputs = f.read().splitlines()

for line in inputs:
    print(line)

# Part one.
result1 = 0
print(f"result1 is {result1}")

# Part two.
result2 = 0
print(f"result2 is {result2}")
