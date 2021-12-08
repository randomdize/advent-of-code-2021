#!/usr/bin/env python3
import sys
import numpy

filename = "input"

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    inputs = f.read().splitlines()

# Part one.


def most_common_bit(inputs, location):
    one = 0
    zero = 0
    for line in inputs:
        if line[location] == '0':
            zero += 1
        else:
            one += 1
    if one >= zero:
        # modified for part 2. 
        # When 0 and 1 is equally common, keep values with 1.
        return '1'
    else:
        return '0'


def flipbits(binaryinput):
    r = ""
    for ch in binaryinput:
        if ch == '0':
            r += '1'
        else:
            r += '0'
    return r


result1 = 0
gamma_binary = ""
for i in range(0, len(inputs[0])):
    gamma_binary += most_common_bit(inputs, i)
gamma = int(gamma_binary, 2)
epsilon = int(flipbits(gamma_binary), 2)
result1 = gamma * epsilon
print(f"result1 is {result1}")

# Part two.
result2 = 0

oxygenSpace = inputs.copy()
oindex = 0
while len(oxygenSpace) > 1:
    selectBit = most_common_bit(oxygenSpace, oindex)
    oxygenSpace = list(filter(lambda v: v[oindex] == selectBit, oxygenSpace))
    oindex += 1

co2Space = inputs.copy()
cindex = 0
while len(co2Space) > 1:
    # Don't need to consider the situation when 0 is equal to 1 
    # because we are going to flip the bit anyway.
    selectBit = flipbits(most_common_bit(co2Space, cindex))
    co2Space = list(filter(lambda v: v[cindex] == selectBit, co2Space))
    cindex += 1

oxygen_generator_rating = int(oxygenSpace[0],2)
co2_scrubber_rating = int(co2Space[0],2)
result2 = oxygen_generator_rating * co2_scrubber_rating
print(f"result2 is {result2}")
