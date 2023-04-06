
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

cnt = 0
def dfs(vertex):
    global cnt

    for curr_v in arr[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True  # 얘 빠뜨림
dfs(1)
print(cnt)