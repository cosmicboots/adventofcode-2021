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
    chart = [[0 for x in range(size_x + 1)] for y in range(size_y + 1)]
    return chart


def graph_line(chart, line):
    print("Line:", line)
    line.sort()
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            return chart
    # List out the x and y values that will need a marking
    x = [x for x in range(line[0][0], line[1][0] + 1)]
    y = [y for y in range(line[0][1], line[1][1] + 1)]
    # Zip the two lists together
    print("X:", x, "Y:", y)
    if len(x) >= len(y):
        xy = [(x, y[i % len(y)]) for i, x in enumerate(x)]
    else:
        xy = [(x[i % len(x)], y) for i, y in enumerate(y)]
    print(xy)
    for x, y in xy:
        chart[y][x] = chart[y][x] + 1
    return chart


def part1():
    """Solution for part one of day05"""
    with open("day05.in", "r") as f:
        paths = ingest([line.rstrip() for line in f])
    chart = build_chart(paths)
    for path in paths:
        chart = graph_line(chart, path)
    for line in chart:
        for point in line:
            if point != 0:
                print(point, end="")
            else:
                print(".", end="")
        print()
    count = 0
    for line in chart:
        for pt in line:
            count += 1 if pt >= 2 else 0
    print(count)


def main():
    print("=== PART 1 ===")
    part1()


if __name__ == "__main__":
    main()
