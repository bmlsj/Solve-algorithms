from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

node = [[] for _ in range(n + 1)]
for _ in range(m):  # 방문한 노드 입력
    a, b = (map(int, sys.stdin.readline().split()))
    node[a].append(b)
    node[b].append(a)
    node[a].sort()  # 노드 정렬  ex) [4, 1] => [1, 4]
    node[b].sort()


def bfs(node, start, visited):
    ans = []
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()

        for i in node[now]:
            if not visited[i]:
                visited[i] = True
                cnt[i] = cnt[now] + 1
                queue.append(i)

                if cnt[i] == k:
                    ans.append(i)

    if len(ans) == 0:
        print(-1)
    else:
        for i in ans:
            print(i)


cnt = [0 for _ in range(n + 1)]
visited = [False] * (n + 1)
bfs(node, x, visited)
# print(cnt)

# check = False
# for i in range(1, len(cnt)):
#     if cnt[i] == k and i != x:
#         print(i)
#         check = True
#
# if not check:
#     print(-1)
