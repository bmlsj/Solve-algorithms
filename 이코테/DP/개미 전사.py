n = int(input())
food = list(map(int, input().split()))

## bottom-up : 상향식
d = [0] * (n+1)

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[n-1])


## top-down : 하향식
dp = {0: food[0], 1: max(food[0], food[1])}
for i in range(2, len(food)):
    dp[i] = food[i]

def ant(x):
    if x in dp.keys():
        return dp[x]

    for i in range(2, len(food)):
        dp[i] = max(ant(i - 1), ant(i - 2) + food[i])

    return dp[x-1]


print(ant(n))
