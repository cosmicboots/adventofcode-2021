def ingest(input):
    paths = []
    for line in input:
        print(line)
        paths.append([[int(x) for x in point.split(",")] for point in
                      line.split(" -> ")])
    return paths


def part1():
    with open("day05.in", "r") as f:
        paths = ingest([line.rstrip() for line in f])
    print([[x[0][0], x[1][0]] for x in paths])
    print(paths)


def main():
    print("=== PART 1 ===")
    part1()


if __name__ == "__main__":
    main()
