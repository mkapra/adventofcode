#!/usr/bin/env python3

import numpy as np


FILENAME = 'input.txt'
# FILENAME = 'input_test.txt'


def get_calories():
    i = 1
    calories = {}

    with open(FILENAME) as fh:
        while line := fh.readline():
            if line == '\n':
                i += 1
                continue

            if i in calories:
                calories[i] = calories[i] + int(line)
                continue

            calories[i] = int(line)

    return calories


def part_one():
    calories = get_calories()
    max_calories = max(calories.values())
    max_elve = [k for k, v in calories.items() if v == max_calories][0]
    print(f"elve={max_elve} calories={max_calories}")


def part_two():
    calories = get_calories()
    max_three_calories = sum(np.sort([f for f in calories.values()])[-3:])
    print(f"Max three calories={max_three_calories}")


part_two()
