import argparse
import math

all_cubes = {"r": 12, "g": 13, "b": 14}
color_lens = {"r": 3, "g": 5, "b": 4}


def is_game_possible(line: str) -> int:
    linelen = len(line)
    id1 = line.find(" ")
    i = line.find(":")
    game_id = int(line[id1:i])

    while i < linelen - 1:
        # Check each cube color and see if this breaks constraint.
        # Start at previous seperator and end at next seperator.
        id1 = i + 2
        id2 = line.find(" ", id1)
        digit = line[id1:id2]
        color = line[id2 + 1]

        if int(digit) > all_cubes[color]:
            return 0

        i += len(digit) + color_lens[color] + 3

    return game_id


def get_smallest_power(line: str) -> int:
    linelen = len(line)
    id1 = line.find(" ")
    i = line.find(":")
    smallest_possible = {"r": 0, "g": 0, "b": 0}

    while i < linelen - 1:
        # Check value of each cube color and see if this exceeds smallest possible.
        # Start at previous seperator and end at next seperator.
        id1 = i + 2
        id2 = line.find(" ", id1)
        digit = line[id1:id2]
        color = line[id2 + 1]

        num = int(digit)
        if num > smallest_possible[color]:
            smallest_possible[color] = num

        i += len(digit) + color_lens[color] + 3

    power = 1
    for item in smallest_possible.values():
        power *= item

    return power


def problem_1(input_path):
    n_possible = 0

    with open(input_path, "r") as f:
        while line := f.readline():
            n_possible += is_game_possible(line)

    print(n_possible)


def problem_2(input_path):
    powersum = 0

    with open(input_path, "r") as f:
        while line := f.readline():
            powersum += get_smallest_power(line)

    print(powersum)


def main(problem, input_path):
    if problem == "p1":
        problem_1(input_path)

    elif problem == "p2":
        problem_2(input_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem")
    parser.add_argument("input_path")

    args = parser.parse_args()
    main(args.problem, args.input_path)
