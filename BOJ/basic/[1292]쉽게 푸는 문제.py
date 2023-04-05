a, b = map(int, input().split())

num = []
for i in range(1, b + 1):
    for j in range(i):
        num.append(str(i))

sum_value = 0
for i in range(a - 1, b):
    sum_value += int(num[i])

print(sum_value)


# 정수형으로 변환
num = []
for i in range(1, b + 1):
    for j in range(i):
        num.append(i)

print(sum(num[a-1:b]))