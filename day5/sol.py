import argparse


def problem_1(input_path):
    # Assume maps are ordered in input.
    # I.e. "a-to-b" is always followed by "b-to-c".

    with open(input_path) as f:
        lines = f.readlines()

    sources = list(map(int, lines[0].split()[1:]))

    n_sources = len(sources)
    n_lines = len(lines)

    i_line = 2
    while i_line < n_lines:
        j_line = i_line + 1

        change_list = []  # src_idx, offset
        while (j_line < n_lines) and (lines[j_line] != "\n"):
            dst_start, src_start, range_len = map(int, lines[j_line].split())
            for i_src in range(n_sources):
                if src_start <= sources[i_src] < src_start + range_len:
                    change_list.append((i_src, dst_start - src_start))

            j_line += 1

        for i_src, offset in change_list:
            sources[i_src] += offset

        i_line = j_line + 1

    print(min(sources))


def problem_2(input_path):
    # Assume maps are ordered in input.
    # I.e. "a-to-b" is always followed by "b-to-c".

    with open(input_path) as f:
        lines = f.readlines()

    # Sources: [(start, end)]
    sources = list(map(int, lines[0].split()[1:]))
    sources = [
        [sources[i], sources[i] + sources[i + 1]]
        for i in range(0, len(sources) // 2 + 1, 2)
    ]
    sources.sort()
    print(sources)

    n_sources = len(sources)
    n_lines = len(lines)

    i_line = 2
    while i_line < n_lines:
        j_line = i_line + 1

        destinations = []  # [(src_map_start, src_map_end, offset)]
        while (j_line < n_lines) and (lines[j_line] != "\n"):
            dst_map_start, src_map_start, map_len = map(int, lines[j_line].split())
            src_map_end = src_map_start + map_len
            offset = dst_map_start - src_map_start
            print("<", lines[j_line].split(), ">", src_map_start, src_map_end)

            destinations.append((src_map_start, src_map_end, offset))
            j_line += 1

        destinations.sort()
        n_destinations = len(destinations)

        i_src = 0
        i_dst = 0

        while i_src < n_sources and i_dst < n_destinations:
            src_start, src_end = sources[i_src]
            src_map_start, src_map_end, offset = destinations[i_dst]

            print(src_start, src_end, src_map_start, src_map_end)
            new_sources = []

            if src_end <= src_map_start:
                i_src += 1
                continue

            if src_start >= src_map_end:
                i_dst += 1
                continue

            if src_start < src_map_start:
                if src_end <= src_map_end:
                    sources[i_src][1] = src_map_start
                    new_sources.append([src_start + offset, src_map_start + offset])
                    i_src += 1

                else:
                    sources[i_src][0] = src_map_end
                    new_sources.append([src_start, src_map_start])
                    new_sources.append([src_map_start + offset, src_map_end + offset])
                    i_dst += 1

            else:
                if src_end <= src_map_end:
                    sources[i_src][0] += offset
                    sources[i_src][1] += offset
                    i_src += 1

                else:
                    sources[i_src][0] = src_map_end
                    new_sources.append([src_start + offset, src_map_end + offset])
                    i_dst += 1

        sources.extend(new_sources)
        sources.sort()

        print(sources)

        i_line = j_line + 1

    # print(sources)

    # print(min(sources))


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
