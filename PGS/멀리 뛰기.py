def solution(n):

    # 1-> 1
    # 2 -> 2
    # 3 -> 3
    # 4 -> 5
    # 5 -> 8

    # ak =  ak-1 + k - 1
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp)
    return dp[n-1] % 1234567

print(solution(4))
