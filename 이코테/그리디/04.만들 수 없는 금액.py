from itertools import combinations

n = int(input())
m = list(map(int, input().split()))

c = []
for i in range(2, n+1):
    c.append(list(combinations(m, i)))

n = []
for i in range(len(c)):
    for j in range(len(c[i])):
        n.append(sum(c[i][j]))

n = list(set(n))

for i in range(1, n[-1]):
    if (i+1) not in n:
        print(i+1)
        break

