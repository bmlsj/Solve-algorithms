from collections import deque
import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for p in range(1, t + 1):

    ## DFS로 풀이
    def dfs(x, y, now):

        if len(now) == 7:
            num.add(now)
            return

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, now + arr[nx][ny])

    for k in range(4):
        for j in range(4):
            dfs(k, j, arr[k][j])

    ## BFS로 풀이
    def bfs(x, y):
        q = deque([(x, y, arr[x][y])])

        while q:
            a, b, now = q.popleft()

            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if len(now) == 7:
                    num.add(now)
                    continue

                if 0 <= nx < 4 and 0 <= ny < 4:
                    q.append([nx, ny, now + arr[nx][ny]])

    for k in range(4):
        for j in range(4):
            bfs(k, j)

    arr = [list(input().split()) for _ in range(4)]
    num = set()
print(f"#{p} {len(num)}")
