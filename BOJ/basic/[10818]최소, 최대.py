
n = int(input())
num = list(map(int, input().split()))

# max, min 함수 사용시
print(min(num), max(num))


# 내장함수 사용하지 않았을 경우
max_num = num[0]
min_num = num[0]
for i in range(len(num)):
    if max_num <= num[i]:
        max_num = num[i]
    elif min_num >= num[i]:
        min_num = num[i]

print(min_num, max_num)