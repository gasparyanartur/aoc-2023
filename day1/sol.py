from typing import Iterable
import argparse

word_to_digit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_first_digit(line: Iterable[str], include_word: bool = False) -> str:
    for char in line:
        if "0" <= char <= "9":
            return char


def find_first_digit_with_word_left(line: Iterable[str]) -> str:
    for i, char in enumerate(line):
        if "0" <= char <= "9":
            return char

        for word_len in range(5, 2, -1):
            if i >= word_len - 1:
                word = line[i - (word_len - 1): i + 1]
                digit = word_to_digit.get(word)
                if digit:
                    return digit


def find_first_digit_with_word_right(line: Iterable[str]) -> str:
    line_len = len(line)
    for i in range(line_len - 1, -1, -1):
        char = line[i]
        if "0" <= char <= "9":
            return char

        for word_len in range(5, 2, -1):
            if i <= line_len - word_len:
                word = line[i : i + word_len]
                digit = word_to_digit.get(word)
                if digit:
                    return digit


def main(problem, input_path):
    if problem == "p1":
        problem_1(input_path)

    elif problem == "p2":
        problem_2(input_path)


def problem_1(input_path):
    cum_sum = 0
    with open(input_path) as f:
        while line := f.readline():
            left_digit = find_first_digit(line)
            right_digit = find_first_digit(line[::-1])
            digit = left_digit + right_digit
            cum_sum += int(digit)

    print(cum_sum)


def problem_2(input_path):
    cum_sum = 0
    with open(input_path) as f:
        while line := f.readline():
            left_digit = find_first_digit_with_word_left(line)
            right_digit = find_first_digit_with_word_right(line)
            digit = left_digit + right_digit
            cum_sum += int(digit)

    print(cum_sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem")
    parser.add_argument("input_path")

    args = parser.parse_args()
    main(args.problem, args.input_path)
