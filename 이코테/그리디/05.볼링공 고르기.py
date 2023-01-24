from itertools import permutations, combinations

n, m = map(int, input().split())
ball = list(map(int, input().split()))
# print(ball)

idx = [i for i in range(1, len(ball) + 1)]
choose = list(set(combinations(idx, 2)))
# print(choose)

cnt = 0

for i in range(len(choose)):
    if ball[choose[i][0] - 1] != ball[choose[i][1] - 1]:
        cnt += 1

print(cnt)
