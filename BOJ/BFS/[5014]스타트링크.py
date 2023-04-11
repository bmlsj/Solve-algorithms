from collections import deque
import sys

# f : 총 건물 층수, g : 목표 위치, s : 현재 위치
# U : 위로 u층 만큼 이동, D : 아래로 d층 만큼 이동

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        x = queue.popleft()

        if x == g:
            return visited[x] - 1

        move = [u, -d]
        for i in range(2):
            mv = x + move[i]

            if 0 < mv <= f and visited[mv] == 0:
                visited[mv] = visited[x] + 1
                queue.append(mv)

    return "use the stairs"


print(bfs(s))
