import argparse


def problem_1(input_path):
    ...


def problem_2(input_path):
    ...


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
