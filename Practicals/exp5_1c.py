for i in range(4):
    for j in range(i):
        print(" ", end="")
    for j in range(7 - 2*i):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()