a=int(input(""))
for j in range(a):
    for k in range(1, 6 - j):
        if k==5:
            continue
        else:
            print(k, end="")
    for l in range(j):
        print("*", end="")
    for i in range(5 - j, 0, -1):
        print(i, end="")
    print("")

