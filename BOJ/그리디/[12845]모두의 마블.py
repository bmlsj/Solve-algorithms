
## 카드 합성 - 카드의 레벨 합만큼 골드를 받음
# 1. 두 카드는 인접한 카드여야함
# 2. 업글된 A의 레벨은 변하지 않는다.

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

gold, lv = 0, 0

while True:

    first, end = nums[0], nums.pop()
    gold += (first + end)
    lv = max(first, end)

    nums.remove(first)
    if len(nums) == 0:
        break
    nums.append(lv)

print(gold)