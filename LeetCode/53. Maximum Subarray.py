
# subarray : 각 원소들의 합이 최대가 되는 연속적인 부분 배열
def maxSubArray(nums) -> int:
    dp = nums.copy()
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
