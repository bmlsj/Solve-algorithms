T = int(input())
for tc in range(1, T + 1):

    init = list(input())
    n = ['0'] * len(init)
    cnt = 0

    for i in range(len(n)):
        if n[i] != init[i]:
            n[i:] = init[i] * len(n[i:])
            cnt += 1

    print('#{} {}'.format(tc, cnt))

t = int(input())

for i in range(1, t + 1):

    n = list(input())
    l = len(n)
    start = ['0'] * l
    cnt = 0
    zero_idx = 0

    while n != start:

        idx = n.index('1', zero_idx, l)
        cnt += 1
        for a in range(idx, l):
            start[a] = '1'

        if n == start:
            break

        zero_idx = n.index('0', idx, l)
        cnt += 1
        for a in range(zero_idx, l):
            start[a] = '0'

    print(f"#{i} {cnt}")
