import sys

input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

# for i in range(n):
#     stair[i] = int(input())

if n > 2:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

    for i in range(3, n):
        dp[i] = max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3])

    print(dp[n - 1])

elif n == 2:
    print(max(stair[0], stair[0] + stair[1]))
else:
    print(stair[0])


