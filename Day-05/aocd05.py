with open("input05.txt") as f:
    coord_system = [[0]*1000 for _ in range(1000)]
    lines = f.readlines()
    for l in range(len(lines)):
        new_line = lines[l].strip("\n")
        coord_pairs = new_line.split(" -> ")
        x1, y1 = map(int, coord_pairs[0].split(","))
        x2, y2 = map(int,coord_pairs[1].split(","))
        # Since nested lists flip x and y, need to account for it here
        if y1 == y2:
            # Horizontal line
            print("Horizontal line")
            if x2 > x1:
                for i in range(x1, x2+1):
                    coord_system[y1][i] += 1
            else:
                for i in range(x2, x1+1):
                    coord_system[y1][i] += 1

        elif x1 == x2:
            # Vertical line
            print("Vertical line")
            if y2 > y1:
                for j in range(y1, y2+1):
                    coord_system[j][x1] += 1
            else:
                for j in range(y2, y1+1):
                    coord_system[j][x1] += 1
        else:
            # Diagonal line
            print("Diagonal line")
            if x2 > x1:
                if y2 > y1:
                    while x1 <= x2:
                        coord_system[y1][x1] += 1
                        x1 += 1
                        y1 += 1
                else:
                    while x1 <= x2:
                        coord_system[y1][x1] += 1
                        x1 += 1
                        y1 -= 1
            elif x1 > x2:
                if y2 > y1:
                    while x1 >= x2:
                        coord_system[y1][x1] += 1
                        x1 -= 1
                        y1 += 1
                else:
                    while x1 >= x2:
                        coord_system[y1][x1] += 1
                        x1 -= 1
                        y1 -= 1
    res = 0
    for col in coord_system:
        print(list(filter(lambda x: x > 1, col)))
        res += len(list(filter(lambda x: x > 1, col)))
    print(res)




