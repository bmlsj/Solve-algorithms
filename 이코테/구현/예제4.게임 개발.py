n, m = map(int, input().split())  # n x m 맵 생성
x, y, direction = map(int, input().split())  # 0 - 북, 1 - 동, 2 - 남, 3 - 서
game_map = []

for _ in range(n):
    game_map.append(list(map(int, input().split())))  # 0 - 육지 / 1 - 바다

game_map[x][y] = 1


def turn90():
    turn_map = []
    for i in range(n - 1, -1, -1):
        map_row = []
        for j in range(m):
            map_row.append(game_map[j][i])
        turn_map.append(map_row)
    return turn_map


# start
visit = 0
if game_map[x][y - 1] == 0:
    game_map = turn90()
    game_map[x][y - 1] = 1
    visit += 1

else:
    game_map = turn90()

if game_map[x - 1][y] and game_map[x + 1][y] and game_map[x][y - 1] and game_map[x][y + 1]:
    game_map[x][y+1] = 1