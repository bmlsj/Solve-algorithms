# bfs
# https://leetcode.com/problems/map-of-highest-peak/
from collections import deque


def highestPeak(isWater):
    m = len(isWater)
    n = len(isWater[0])

    # 0은 water, 1은 land
    # 인접하는 땅의 수 만큼 구해 height가 가장 높은 것 구하기

    # 높이를 기록하는 2차원 배열 - 초기화
    height = [[0 for _ in range(n)] for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = set()
    queue = deque([])
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                queue.append([[i, j], 0])
                visited.add((i, j))

    while queue:
        curr, value = queue.popleft()
        x, y = curr
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            if 0 <= nx < m and 0 <= ny < n:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append([[nx, ny], value + 1])
                    height[nx][ny] = value + 1

    return height


Map = [[0, 1], [0, 0]]
print(highestPeak(Map))
