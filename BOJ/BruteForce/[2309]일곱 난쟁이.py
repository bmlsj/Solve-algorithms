from itertools import combinations

"""
nan_jang = []
for _ in range(9):
    nan_jang.append(int(input()))

select_seven = list(combinations(nan_jang, 7))

for i in select_seven:
    if sum(i) is 100:
        ans = list(i)
        break

ans.sort()
for i in ans:
    print(i)
"""

height = []
for _ in range(9):
    height.append(int(input()))

nanjang = list(combinations(height, 2))
for i in nanjang:
    if sum(height) - sum(i) == 100:
        height.remove(i[0])
        height.remove(i[1])

height = sorted(height)
for i in height:
    print(i)
