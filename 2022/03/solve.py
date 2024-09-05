#!/usr/bin/env python3

import string


# FILENAME = 'input_test.txt'
FILENAME = 'input.txt'

words = list(string.ascii_lowercase)
[words.append(w) for w in string.ascii_uppercase]

priorities = list(range(1, 53))


def part_one():
    with open(FILENAME) as fh:
        appears_in_both = []
        while backpack := fh.readline().strip():
            middle = int(len(backpack) / 2)
            first_comp, sec_comp = backpack[:middle], backpack[middle:]
            for f in first_comp:
                if f in sec_comp:
                    appears_in_both.append(f)
                    break

        calc_prio = sum([priorities[words.index(b)] for b in appears_in_both])
        print(f"Sum of priorities: {calc_prio}")


def part_two():
    with open(FILENAME) as fh:
        appears_in_both = []
        backpacks = [line.strip() for line in fh]
        for i in range(0, len(backpacks), 3):
            found = False
            grouped_backpacks = backpacks[i:i+3]
            for i, backpack in enumerate(grouped_backpacks):
                if found:
                    break

                for item in backpack:
                    if item in grouped_backpacks[(i+1) % 3] and \
                            item in grouped_backpacks[(i + 2) % 3]:
                        appears_in_both.append(item)
                        found = True
                        break

            found = False

        calc_prio = sum([priorities[words.index(b)] for b in appears_in_both])
        print(f"Sum of priorities: {calc_prio}")


part_one()
part_two()
