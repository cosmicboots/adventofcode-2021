pos = [0, 0]
direction_key = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
with open("day02.in") as f:
    # fa = [i for i in f]
    for x in f:
        cmd = x.split()[0]
        val = int(x.split()[1])
        pos[0] += direction_key[cmd][0] * val
        pos[1] += direction_key[cmd][1] * val

print("Current position:", pos)
print("Product:", pos[0] * pos[1])

# Part 2
pos = [0, 0, 0]
with open("day02.in2") as f:
    for x in f:
        cmd = x.split()[0]
        val = int(x.split()[1])
        if cmd == "down":
            pos[2] += val
        elif cmd == "up":
            pos[2] -= val
        elif cmd == "forward":
            pos[0] += val
            pos[1] += pos[2] * val

print("Current position:", pos)
print("Product:", pos[0] * pos[1])
