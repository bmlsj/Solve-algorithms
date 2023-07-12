import sys
input = sys.stdin.readline

# 문제 조건을 잘 읽을 것

n = int(input())

for i in range(1, n + 1):
    tmp = i
    for num in str(i):
        tmp += int(num)

    if tmp == n:
        print(i)
        break

    if i == n:
        print(0)
