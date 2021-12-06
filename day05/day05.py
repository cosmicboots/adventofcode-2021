def ingest(input):
    """Parse the input data and load it into a working datastructure to solve
    the problem"""
    paths = []
    for line in input:
        print(line)
        paths.append([[int(x) for x in point.split(",")] for point in
                      line.split(" -> ")])
    return paths


def build_chart(paths):
    """Create an empty table using the largest x and y values"""
    size_x = max([x[0][0] for x in paths] + [x[1][0] for x in paths])
    size_y = max([y[0][1] for y in paths] + [y[1][1] for y in paths])
    chart = [[0 for x in range(size_x)] for y in range(size_y)]
    return chart


def part1():
    """Solution for part one of day05"""
    with open("day05.in", "r") as f:
        paths = ingest([line.rstrip() for line in f])
    chart = build_chart(paths)
    [print(line) for line in chart]


def main():
    print("=== PART 1 ===")
    part1()


if __name__ == "__main__":
    main()
