import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for i in range(1, 11):

    _, b = map(int, input().split())
    arr = list(map(int, input().split()))
    way = [[] for _ in range(100)]
    visited = [False] * 100

    for j in range(0, b * 2, 2):
        way[arr[j]].append(arr[j+1])

    def bfs(v):

        q = deque([v])

        while q:
            a = q.popleft()

            for k in way[a]:
                if k == 99:
                    return True

                if not visited[k]:
                    q.append(k)
        return False

    visited[0] = True
    print(f"#{i} {1 if bfs(0) else 0}")

