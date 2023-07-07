import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if numlist[j] > numlist[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n - max(dp))
