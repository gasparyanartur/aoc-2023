import argparse


def problem_1(input_path):
    with open(input_path) as f:
        lines = f.readlines()

    sum_winning = 0
    for line in lines:
        i1 = line.find(":")
        i2 = line.find("|", i1 + 1)
        winning_nums = set(line[i1 + 1 : i2].split())
        player_nums = line[i2 + 1 :].split()

        n_match = len(winning_nums.intersection(player_nums))
        score = (1 << (n_match - 1)) if (n_match > 0) else 0
        sum_winning += score

    print(sum_winning)


def problem_2(input_path):
    with open(input_path) as f:
        lines = f.readlines()

    cards = []
    for line in lines:
        i1 = line.find(":")
        i2 = line.find("|", i1 + 1)
        winning_nums = set(line[i1 + 1 : i2].split())
        player_nums = line[i2 + 1 :].split()

        n_match = len(winning_nums.intersection(player_nums))
        cards.append([n_match, 1])  # (Number of matches, number of copies)

    card_count = 0
    for i, (n_match, n_copies) in enumerate(cards):
        card_count += n_copies
        for j in range(i + 1, i + 1 + n_match):
            cards[j][1] += n_copies

    print(card_count)


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
