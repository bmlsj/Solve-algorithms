
n, m = map(int, input().split())
nums = list(map(int, input().split()) for _ in range(n))

min_list = []
for i in range(n):
    min_list.append(min(nums[i]))

print(max(min_list))

