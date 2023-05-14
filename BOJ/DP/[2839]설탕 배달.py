import sys
input = sys.stdin.readline
INF = 5001

n = int(input())
group = [3, 5]

dp = [INF] * (n + 1)
dp[0] = 0

for g in group:
    for i in range(g, n + 1):
        dp[i] = min(dp[i], dp[i - g] + 1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])
