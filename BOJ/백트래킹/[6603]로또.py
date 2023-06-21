import sys
input = sys.stdin.readline

def dfs(v, cnt):

    if cnt == 6:
        print(*order)
        return

    for i in range(v, k):
        order.append(select[i])
        dfs(i+1, cnt+1)
        order.pop()


while True:
    k, *select = map(int, input().split())

    if k == 0:
        break

    order = []
    dfs(0, 0)
    print()
