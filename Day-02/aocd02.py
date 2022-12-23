with open("input02.txt") as f:
    # ---------- Part 1 ----------
    lines = f.readlines()
    dirs = {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}
    pos = [0,0]
    for line in lines:
        line = line.split()
        pos[0] += dirs[line[0]][0] * int(line[1])
        pos[1] += dirs[line[0]][1] * int(line[1])
    print(pos[0] * pos[1])

    # ---------- Part 2 ----------
    aim = 0
    pos = [0,0]
    for line in lines:
        line = line.split()
        if line[0] == "up":
            aim -= int(line[1])
        elif line[0] == "down":
            aim += int(line[1])
        else:
            pos[0] += int(line[1])
            pos[1] += aim * int(line[1])
    print(pos[0] * pos[1])



