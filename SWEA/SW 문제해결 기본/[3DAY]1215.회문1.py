import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for i in range(1, 11):

    n = int(input())

    arr = [list(input()) for _ in range(8)]
    cnt = 0
    queue = deque()


    def length(x, y, k1, k2):
        global sen, cnt
        queue.append([x, y])

        while queue:
            a, b = queue.popleft()
            sen += arr[a][b]
            dx, dy = a + k1, b + k2

            if len(sen) == n:
                if sen == sen[::-1]:
                    cnt += 1
                return

            if 0 <= dx < 8 and 0 <= dy < 8:
                queue.append([dx, dy])

    for j in range(8):
        for k in range(8):
            sen = ""
            length(j, k, 0, 1)

    for j in range(8):
        for k in range(8):
            sen = ""
            length(j, k, 1, 0)


    print(f"#{i} {cnt}")
