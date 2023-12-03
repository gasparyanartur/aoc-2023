import argparse


def problem_1(input_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    h = len(lines)
    w = len(lines[0]) - 1  # Ignore '\n'
    y = 0

    symbols = []  # (x, y)
    numbers = []  # (x1, x2, y)

    # Parse symbols and numbers
    while y < h:
        x = 0

        while x < w:
            while x < w and lines[y][x] == ".":  # Skip whitespace
                x += 1

            if x == w:  # Check OOB
                continue

            if not lines[y][x].isdigit():  # Found symbol
                symbols.append((x, y))
                x += 1
                continue

            # Found number
            x1 = x
            while x < w and lines[y][x].isdigit():
                x += 1
            x2 = x - 1

            numbers.append((x1, x2, y))

        y += 1

    # Find all numbers which have symbol in vicinity
    partsum = 0
    for nx1, nx2, ny in numbers:
        for sx, sy in symbols:
            if ((sx == nx1 - 1 or sx == nx2 + 1) and (ny - 1 <= sy <= ny + 1)) or (
                (nx1 - 1 <= sx <= nx2 + 1) and (sy == ny - 1 or sy == ny + 1)
            ):
                number = int(lines[ny][nx1 : nx2 + 1])
                partsum += number

    print(partsum)


def problem_2(input_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    h = len(lines)
    w = len(lines[0]) - 1  # Ignore '\n'
    y = 0

    gears = []  # (x, y)
    numbers = []  # (x1, x2, y)

    # Parse symbols and numbers
    while y < h:
        x = 0

        while x < w:
            while x < w and lines[y][x] == ".":  # Skip whitespace
                x += 1

            if x == w:  # Check OOB
                continue

            if not lines[y][x].isdigit():  # Found symbol
                if lines[y][x] == "*":  # Found symbol
                    gears.append((x, y))

                x += 1
                continue

            # Found number
            x1 = x
            while x < w and lines[y][x].isdigit():
                x += 1
            x2 = x - 1

            numbers.append((x1, x2, y))

        y += 1

    # Find all gears which have adjacent numbers
    gearratio = 0

    for sx, sy in gears:
        adjacents = []
        for nx1, nx2, ny in numbers:
            if ((sx == nx1 - 1 or sx == nx2 + 1) and (ny - 1 <= sy <= ny + 1)) or (
                (nx1 - 1 <= sx <= nx2 + 1) and (sy == ny - 1 or sy == ny + 1)
            ):
                adjacents.append((nx1, nx2, ny))

        clean_pairs = set()
        for adjacent1 in adjacents:
            for adjacent2 in adjacents:
                if (
                    (adjacent1 == adjacent2)
                    or ((adjacent1, adjacent2) in clean_pairs)
                    or ((adjacent2, adjacent1) in clean_pairs)
                ):
                    continue

                clean_pairs.add((adjacent1, adjacent2))

        if len(clean_pairs) == 1:
            ((nx1, nx2, ny), (nnx1, nnx2, nny)) = next(iter(clean_pairs))
            number1 = int(lines[ny][nx1 : nx2 + 1])
            number2 = int(lines[nny][nnx1 : nnx2 + 1])
            gearratio += number1 * number2

    print(gearratio)


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
