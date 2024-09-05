#!/usr/bin/env python3

# FILENAME = 'input_test.txt'
FILENAME = 'input.txt'


def line_to_ranges(line):
    first_range, second_range = line.split(',')
    first_range_from, first_range_to = first_range.split('-')
    second_range_from, second_range_to = second_range.split('-')

    return range(int(first_range_from), int(first_range_to) + 1), \
        range(int(second_range_from), int(second_range_to) + 1)


def order_ranges(first_range, second_range):
    if len(first_range) > len(second_range):
        return second_range, first_range
    else:
        return first_range, second_range


def part_one():
    i = 0
    with open(FILENAME) as fh:
        while line := fh.readline().strip():
            first_range, second_range = line_to_ranges(line)
            smaller, greater = order_ranges(first_range, second_range)

            not_in = False
            for x in smaller:
                if x not in greater:
                    not_in = True
                    break

            if not not_in:
                i += 1

    print(i)


def part_two():
    i = 0
    with open(FILENAME) as fh:
        while line := fh.readline().strip():
            first_range, second_range = line_to_ranges(line)
            smaller, greater = order_ranges(first_range, second_range)

            is_in = False
            for x in smaller:
                if x in greater:
                    is_in = True
                    break

            if is_in:
                i += 1

    print(i)


# part_one()
part_two()
