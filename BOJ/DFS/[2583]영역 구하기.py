import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for _ in range(k):
    left_X, left_Y, right_X, right_Y = map(int, input().split())

    for i in range(left_Y, right_Y):
        for j in range(left_X, right_X):
            arr[i][j] = 1


def dfs(x, y):

    global cnt
    visited[x][y] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if arr[nx][ny] != 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


visited = [[False] * n for _ in range(m)]
cntlist = []
ans = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and arr[i][j] != 1:
            cnt = 0
            dfs(i, j)
            ans += 1
            cntlist.append(cnt)

cntlist.sort()
print(ans)
for cnt in cntlist:
    print(cnt, end=' ')