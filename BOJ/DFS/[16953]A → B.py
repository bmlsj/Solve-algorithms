import sys

input = sys.stdin.readline().strip()

a, b = map(int, input.split())

ans = -1


def dfs(start, goal, cnt):
    if start == goal:
        global ans
        ans = cnt
    if (start * 10 + 1) <= goal:
        dfs(start * 10 + 1, b, cnt + 1)
    if (start * 2) <= goal:
        dfs(start * 2, b, cnt + 1)


dfs(a, b, 1)
print(ans)
