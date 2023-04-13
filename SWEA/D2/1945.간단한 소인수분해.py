
t = int(input())


for i in range(1, t+1):

    num = int(input())
    n = [2, 3, 5, 7, 11]
    cntList = []
    for k in n:
        cnt = 0
        while True:
            if num % k == 0:
                num //= k
                cnt += 1

            else:
                cntList.append(cnt)
                break

    print(f"#{i}", end=' ')
    for j in cntList:

        print(j, end=' ')
    print()