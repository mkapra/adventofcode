#!/usr/bin/env python3

import re
from dataclasses import dataclass


# FILENAME = 'input_test.txt'
FILENAME = 'input.txt'


@dataclass
class Movement:
    amount: int
    from_stack: int
    to_stack: int

    def exec(self, stacks):
        for i in range(self.amount):
            el = stacks[self.from_stack].pop()
            stacks[self.to_stack].push(el)

    def exec_retain(self, stacks):
        elems = []
        for i in range(self.amount):
            elems.append(stacks[self.from_stack].pop())

        elems.reverse()
        for e in elems:
            stacks[self.to_stack].push(e)


class Stack:
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)

    def pop(self):
        return self.st.pop()

    def __repr__(self):
        return str(self.st)

    def finalize(self):
        self.st.reverse()

    def head(self):
        return self.st[-1]


def init():
    with open(FILENAME) as fh:
        file = [line for line in fh.readlines()]

    # Init stacks
    stacks = {}
    stack_numbers = [nr.strip() for nr in file[file.index('\n') - 1] if nr != " "][:-1]
    for stack_nr in stack_numbers:
        stacks[int(stack_nr)] = Stack()

    stack_pic = file[0:file.index('\n') - 1]
    for i, step in enumerate(range(1, len(stacks) * 4 + 4, 4)):
        for j in range(len(stacks) + 1):
            try:
                if (ele := stack_pic[j][step]) != ' ':
                    stacks[i + 1].push(ele)
            except IndexError:
                pass

    [stack.finalize() for stack in stacks.values()]

    # Execute movements
    movements = file[file.index('\n') + 1:]
    movements = [re.findall(r'\d+', move) for move in movements]
    movements = [Movement(int(m[0]), int(m[1]), int(m[2])) for m in movements]

    return stacks, movements


def part_one():
    stacks, movements = init()
    [m.exec(stacks) for m in movements]
    print("".join([s.head() for s in stacks.values()]))


def part_two():
    stacks, movements = init()
    [m.exec_retain(stacks) for m in movements]
    print("".join([s.head() for s in stacks.values()]))


# part_one()
part_two()
