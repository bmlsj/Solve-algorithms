import sys
from collections import deque
INF = 1e6
sys.stdin = open("input.txt", "r")
t = int(input())

for c in range(1, 11):

    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    q = deque()
    q.append([0, 0])
    distance[0][0] = 0

    def bfs():
        while q:
            a, b = q.popleft()

            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):

                nx = a + dx[i]
                ny = b + dy[i]

                if 0 <= nx < n and 0 <= ny < n:

                    if distance[nx][ny] > distance[a][b] + arr[nx][ny]:
                        distance[nx][ny] = distance[a][b] + arr[nx][ny]  # 더 작은 값으로 교체
                        q.append([nx, ny])

    bfs()
    print(f"#{c} {distance[-1][-1]}")