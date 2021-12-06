#!/usr/bin/env python3
import sys

filename = "input"

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    inputs = f.read().splitlines()

horizontal = 0
depth = 0

# Part one.
result1 = 0


def getStep(line):
    return int(line.split(" ")[1])


for line in inputs:
    if line.startswith("forward"):
        horizontal += getStep(line)
    if line.startswith("down"):
        depth += getStep(line)
    if line.startswith("up"):
        depth -= getStep(line)
result1 = horizontal * depth

print(f"result1 is {result1}")

# Part two.

horizontal = 0
depth = 0
aim = 0

for line in inputs:
    if line.startswith("forward"):
        horizontal += getStep(line)
        depth += aim * getStep(line)
    if line.startswith("down"):
        aim += getStep(line)
    if line.startswith("up"):
        aim -= getStep(line)
result2 = horizontal * depth
print(f"result2 is {result2}")
