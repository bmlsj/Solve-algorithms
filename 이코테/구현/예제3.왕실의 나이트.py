
n = input()  # a1
night = []
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in n:
    night.append(i)
    if night[0] in col:
        night[0] = col.index(night[0]) + 1

move = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]  # 방향 벡터
x, y = night[0], int(night[1])
cnt = 0

for i, j in move:
    x += i
    y += j

    if 1 <= x <= 8 and 1 <= y <= 8:
        cnt += 1

    x, y = night[0], int(night[1])

print(cnt)