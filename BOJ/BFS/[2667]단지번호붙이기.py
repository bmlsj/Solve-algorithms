# 1 : 집이 있는 곳, 0 : 집이 없는 곳
# 단지별 각 집의 수를 출력
from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

## dfs
def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1:
        global cnt
        arr[x][y] = 0
        cnt += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


k = 0
cnt = 0
cnt_list = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            cnt_list.append(cnt)
            k += 1
            cnt = 0

print(k)
cnt_list.sort()
for i in cnt_list:
    print(i)


## bfs
def bfs(x, y):

    q = deque()
    q.append((x, y))

    arr[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

k = 0
cnt_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            k += 1
            cnt_list.append(bfs(i, j))

cnt_list.sort()
print(k)
for i in cnt_list:
    print(i)
