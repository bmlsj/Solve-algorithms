import sys
sys.stdin = open("input.txt", "r")


for i in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    sumlist = []

    for j in range(100):
        ans_row = 0
        ans_col = 0
        ans = 0
        for k in range(100):
            ans_row += arr[k][j]
            ans_col += arr[j][k]
            sumlist.append(ans_row)
            sumlist.append(ans_col)

            if i == j:
                ans += arr[j][k]

            sumlist.append(ans)
            ans = 0
            if abs(i-j) == 100:
                ans += arr[i][j]

            sumlist.append(ans)


    print(f"#{i} {max(sumlist)}")




