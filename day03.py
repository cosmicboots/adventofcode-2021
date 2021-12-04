def common_bit(list, bit, invert=False):
    bit_count = [0, 0]  # count of 0s and 1s respectively
    for x in list:
        if x[bit] == "0":
            bit_count[0] += 1
        elif x[bit] == "1":
            bit_count[1] += 1
    if bit_count[0] <= bit_count[1]:
        return 0 if invert else 1
    else:
        return 1 if invert else 0


def part1():
    with open("day03.in", "r") as f:
        fa = [line.rstrip() for line in f]
        gamma = ""
        epsilon = ""
        for bit in range(len(fa[0])):
            gamma += str(common_bit(fa, bit))
            epsilon += str(common_bit(fa, bit, invert=True))
        gamma_i = int(gamma, 2)
        epsilon_i = int(epsilon, 2)
        print("Gamma:", gamma_i)
        print("Epsilon:", epsilon_i)
        print("Power consumption:", gamma_i * epsilon_i)


def part2():
    with open("day03.in2", "r") as f:
        fa = [line.rstrip() for line in f]
        fb = fa.copy()
        for bit in range(len(fa[0])):
            fa = [x for x in fa if x[bit] == str(common_bit(fa, bit))]
            # Break to stop if we're already down to one result
            if len(fa) == 1:
                break
        for bit in range(len(fb[0])):
            fb = [x for x in fb if x[bit] == str(common_bit(fb, bit,
                  invert=True))]
            if len(fb) == 1:
                break
        oxygen = int(fa[0], 2)
        co2 = int(fb[0], 2)
    print("Oxygen:", oxygen)
    print("CO2:", co2)
    print("Life support rating:", oxygen * co2)


def main():
    print("=== PART 1 ===")
    part1()
    print("=== PART 2 ===")
    part2()


if __name__ == "__main__":
    main()
