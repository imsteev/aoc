input = []
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

import functools
import re

def part1():
    total = 0
    for line in input:
        scorecard = line.split(': ')[1]
        winning_nums_str, my_nums_str = scorecard.split(' | ')

        # numbers are "justified", so we need to split on whitespace, not just a single space.
        winning_nums = re.split(r'\s+', winning_nums_str.strip())
        my_nums = re.split(r'\s+', my_nums_str.strip())

        my_winning_nums = [num for num in my_nums if num in winning_nums]

        # score starts at 1, doubling with each subsequent winning number.
        if len(my_winning_nums) > 0:
            score = 2**(len(my_winning_nums)-1)
            total += score
    
    print(total)

part1()