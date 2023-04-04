n = int(input())
# schedule = []
# for _ in range(n):
#     schedule.append(list(map(int, input().split())))

dp = [0 for i in range(n + 1)]

## bottom up
# for i in range(n):  # i 번째까지 일했을 때 얻는 최대 수익을 계산
#     for j in range(i + schedule[i][0], n + 1):  # j는 i번째 날 상담을 진행할 때, 상담이 가능한 모든 날짜
#         if dp[j] < dp[i] + schedule[i][1]:  # j를 기준으로 상담을 했을 때 얻는 최대 수익을 dp[j]에 저장
#             dp[j] = dp[i] + schedule[i][1]
#
# print(dp[-1])

## top-down
arr = [list(map(int, input().split())) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    # i 일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # i 일에 상담을 하는 것과 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])
