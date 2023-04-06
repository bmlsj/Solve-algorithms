n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]

def dfs(x, y):

    dx, dy = [1, 0], [0, 1]
    # 우, 상
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]

        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visited[x][y] == 1 or arr[x][y] == 0:  # 방문했거나 뱀이 있는 경우 False 출력
        return False
    return True


visited[0][0] = True
dfs(0, 0)
print(visited[n-1][m-1])