import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):

    n = int(input())
    buildings = list(map(int, input().split()))
    arr = [[0] * (255) for _ in range(n)]

    for i in range(n):
        h = buildings[i]
        for j in range(h):
            arr[i][j] = 1

    cnt = 0
    for i in range(n):
        for j in range(255):
            if arr[i][j] == 1:
                if arr[i+1][j] == 0 and arr[i+2][j] == 0 and arr[i-1][j] == 0 and arr[i-2][j] == 0:
                    cnt += 1

    print(cnt)
