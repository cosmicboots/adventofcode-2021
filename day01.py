def calc_inc(x):
    prev = 0
    count = 0
    for i in x:
        if i > prev and prev != 0:
            count += 1
        prev = i
    return count


with open("day01.in", "r") as f:
    fa = [int(i.rstrip()) for i in f]
    count_a = calc_inc(fa)

    win = []
    for i in range(len(fa)):
        if i + 2 < len(fa):
            win.append(sum(fa[i:i+3]))
    count_b = calc_inc(win)

print("Increased", count_a, "times")
print("Increased", count_b, "times")
