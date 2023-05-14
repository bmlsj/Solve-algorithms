import sys
from collections import deque
input = sys.stdin.readline

while True:

    w, h = map(int, input().split())

    if w == h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    ## BFS 풀이
    def bfs(x, y):

        q = deque()
        q.append([x, y])
        while q:
            a, b = q.popleft()
            dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, 1, -1, 1, -1]

            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny]:
                    arr[nx][ny] = 0
                    q.append([nx, ny])

    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
