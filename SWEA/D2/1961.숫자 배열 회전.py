t = int(input())

for i in range(1, t + 1):
    n = int(input())

    arr = list(map(int, input().split()) for _ in range(n))
    reversed_arr = arr

    arrlist = []

    for _ in range(3):
        reversed_arr = reversed_arr[::-1]
        reversed_arr = list(zip(*reversed_arr))

        for j in reversed_arr:
            arrlist.append(j)

    print(f"#{i}")
    for p in range(n):
        for j in range(p, len(arrlist), n):
            for k in range(len(arrlist[j])):
                print(arrlist[j][k], end='')

            print(end=' ')
        print()