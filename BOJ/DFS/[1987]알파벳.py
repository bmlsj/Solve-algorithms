import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(a, b):
    global road
    visited[a][b] = True

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if not visited[nx][ny] and arr[nx][ny] not in road:
            visited[nx][ny] = True
            road.append(arr[nx][ny])
            dfs(nx, ny)

# 처음 시작시만 오른쪽과 아래를 비교됨
# 중간중간 어떤 경로가 더 최대인지 알 수 있는 코드가 없다!!
# https://www.acmicpc.net/board/view/39560 -> 반례 모음
r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
road = []

if r > 1 and arr[0][0] != arr[1][0]:
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    road = [arr[0][0], arr[1][0]]
    # 아래로 갔을 때
    dfs(1, 0)

down_len = len(road)
print(road)

# 오른쪽으로 갔을 때
if c > 1 and arr[0][0] != arr[0][1]:
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    road = [arr[0][0], arr[0][1]]
    dfs(0, 1)

right_len = len(road)
print(road)
if down_len == right_len == 0:
    print(1)
else:
    print(max(down_len, right_len))

"""
8 1
A
B
C
D
E
F
G
H
8

1 1
A
1

2 2
AB
CA
2

3 4
ABCD
AAAE
IHGF
9
"""