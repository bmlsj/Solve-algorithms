import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

while True:

    w, h = map(int, input().split())

    if w == h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    # DFS 풀이
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False

        if arr[x][y] == 1 and not visited[x][y]:
            visited[x][y] = 1
            dx = [1, -1, 0, 0, 1, -1, 1, -1]
            dy = [0, 0, -1, 1, -1, 1, 1, -1]
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                dfs(nx, ny)
            return True

        return False


    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                cnt += 1

    print(cnt)