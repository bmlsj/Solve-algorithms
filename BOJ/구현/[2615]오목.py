import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(19)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            target = board[x][y]  # 1 or 2

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                    cnt += 1

                    if cnt == 5:
                        # 6목 이상인지 체크
                        # 시작 x, y에서 왼쪽 부분 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == target:
                            break
                        # 움직인 부분 nx, ny에서 오른쪽 부분 체크
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == target:
                            break

                        print(target)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)