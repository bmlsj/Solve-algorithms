import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
friend = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


def dfs(v, depth):
    global check
    visited[v] = True

    if depth == 5:
        check = True
        return

    for t in friend[v]:
        if not visited[t]:
            dfs(t, depth + 1)
            visited[t] = False


check = False
visited = [False for _ in range(n + 1)]
for i in range(n):
    dfs(i, 1)
    visited[i] = False
    if check:
        break

print(1 if check else 0)
