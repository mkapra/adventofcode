#!/usr/bin/env python3

from enum import Enum


FILENAME = 'input.txt'
# FILENAME = 'input_test.txt'


class ShapeOpponent(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class ShapeResponse(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class Decision(Enum):
    LOOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


points = {
    ShapeResponse.ROCK: 1,
    ShapeResponse.PAPER: 2,
    ShapeResponse.SCISSORS: 3,
}

wins = [
    (ShapeOpponent.SCISSORS, ShapeResponse.ROCK),
    (ShapeOpponent.PAPER, ShapeResponse.SCISSORS),
    (ShapeOpponent.ROCK, ShapeResponse.PAPER),
]

draws = [
    (ShapeOpponent.SCISSORS, ShapeResponse.SCISSORS),
    (ShapeOpponent.PAPER, ShapeResponse.PAPER),
    (ShapeOpponent.ROCK, ShapeResponse.ROCK),
]

loose = [
    (ShapeOpponent.SCISSORS, ShapeResponse.PAPER),
    (ShapeOpponent.PAPER, ShapeResponse.ROCK),
    (ShapeOpponent.ROCK, ShapeResponse.SCISSORS),
]


def check_draw(opponent: ShapeOpponent, response: ShapeResponse) -> bool:
    for do, dr in draws:
        if opponent == do and response == dr:
            return True


def check_win(opponent: ShapeOpponent, response: ShapeResponse) -> bool:
    for wo, wr in wins:
        if opponent == wo and response == wr:
            return True


def part_one():
    res = 0
    with open(FILENAME) as fh:
        while line := fh.readline().strip():
            opponent, response = line.split(' ')
            opponent = ShapeOpponent(opponent)
            response = ShapeResponse(response)
            print(f"opponent={opponent} response={response}")

            res += points[response]

            if check_draw(opponent, response):
                # 3 points for draw
                res += 3
                print(f"Draw new={res}")
                continue

            if check_win(opponent, response):
                # 6 points for winning
                res += 6
                print(f"Win new={res}")
                continue

            print(f"Loose new={res}")


def part_two():
    res = 0
    with open(FILENAME) as fh:
        while line := fh.readline().strip():
            opponent, decision = line.split(' ')
            opponent = ShapeOpponent(opponent)
            decision = Decision(decision)

            if decision == Decision.DRAW:
                if opponent == ShapeOpponent.ROCK:
                    response = ShapeResponse.ROCK
                elif opponent == ShapeOpponent.PAPER:
                    response = ShapeResponse.PAPER
                elif opponent == ShapeOpponent.SCISSORS:
                    response = ShapeResponse.SCISSORS

                res += 3 + points[response]
                print(f"Draw new={res} response={response}")
                continue

            if decision == Decision.LOOSE:
                for o, r in loose:
                    if opponent == o:
                        response = r
                        break
                res += points[response]
                print(f"Loose new={res} response={response}")
                continue

            if decision == Decision.WIN:
                for o, r in wins:
                    if opponent == o:
                        response = r
                        break
                res += 6 + points[response]
                print(f"Win new={res} response={response}")
                continue

# part_one()
part_two()
