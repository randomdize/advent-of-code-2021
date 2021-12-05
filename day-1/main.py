#!/usr/bin/env python3
with open('input') as f:
    lines = f.read().splitlines()

count1 = 0
count2 = 0
# Part one.
for x in range(1, len(lines)):
    if int(lines[x]) > int(lines[x-1]):
        count1 = count1 + 1
# Part two.
for x in range(3, len(lines)):
    if int(lines[x]) > int(lines[x-3]):
        count2 = count2 + 1
print(f"count1 is {count1}.")
print(f"count2 is {count2}.")
