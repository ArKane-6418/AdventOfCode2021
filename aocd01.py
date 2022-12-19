with open("input01.txt") as f:
    # ---------- Part 1 ----------
    input_data = list(map(int, f.readlines()))
    count = 0
    for i in range(len(input_data)-1):
        if input_data[i+1] > input_data[i]:
            count += 1
    print(count)

    # ---------- Part 2 ----------

    count = 0
    for i in range(1, len(input_data)-2):
        if sum(input_data[i:i+3]) > sum(input_data[i-1:i+2]):
            count += 1
    print(count)
