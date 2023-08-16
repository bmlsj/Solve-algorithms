import sys
input = sys.stdin.readline

c = int(input())

# testcase
def suitable_position(player, power):
    global max_score
    if player == 11:
        max_score = max(max_score, power)
        return

    for i in range(11):
        # 방문하지 않았고, 능력치가 0이 아닌 선수만 체크
        if not visited[i] and powers[player][i]:
            visited[i] = True
            position[player] = i
            suitable_position(player + 1, powers[player][i] + power)
            visited[i] = False
            position[player] = 0


for _ in range(c):
    powers = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    visited = [False] * 11   # 방문 체크
    position = [0] * 11      # 포지션별 적합한 선수 번호

    suitable_position(0, 0)
    print(max_score)
