# 백준 18310
n = int(input())

houses = list(map(int, input().split()))
houses = sorted(houses)


# 이중 for문 => 시간 초과 발생
d = []
for i in range(1, houses[-1] + 1):
    s = 0
    for house in houses:
        if house >= i:
            s += (house - i)
        else:
            s += (i - house)

    d.append(s)

print(d.index(min(d)) + 1)


# 제일 거리가 짧은 값은 중앙값
print(houses[(n-1)//2])