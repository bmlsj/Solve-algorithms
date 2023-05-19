
# k개의 수중 6개를 선택
"""
# 조합으로 풀이
from itertools import combinations
while True:
        k, *arr = map(int, input().split())
        if k == 0:
            break

        a = list(combinations(arr, 6))
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
        print()
"""

def dfs(v, depth):
    if depth == 6:
        print(*order)
        return

    for i in range(v, k):     # k개의 입력받은 배열의 원소를 돈다.
        order.append(arr[i])  # 방문한 후, 그 값을 order에 추가한다.
        dfs(i+1, depth+1)     # 깊이+1과 index+1을 해주고 다시 돈다
        order.pop()           # 다 돌았으면 그 값을 지워준다.

while True:
    k, *arr = map(int, input().split())
    if k == 0:
        break

    order = []
    dfs(0, 0)
    print()