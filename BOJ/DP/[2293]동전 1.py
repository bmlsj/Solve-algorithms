## https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2293%EB%B2%88.-%EB%8F%99%EC%A0%84-1-bfi120m5


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for c in coin:
    for i in range(k + 1):
        if i - c >= 0:
            dp[i] += dp[i - c]

print(dp[k])
