n = int(input())
direction = list(input().split())
start = [1, 1]

for i in direction:
    if i == 'R':
        start[1] += 1
        if start[1] < 1 or start[1] > n:
            start[1] -= 1

    elif i == 'U':
        start[0] -= 1
        if start[0] < 1 or start[0] > n:
            start[0] += 1

    elif i == 'D':
        start[0] += 1
        if start[0] < 1 or start[0] > n:
            start[0] -= 1
    else:
        start[1] -= 1
        if start[1] < 1 or start[1] > n:
            start[1] += 1

print(start)
