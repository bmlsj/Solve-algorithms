a, b = map(int, input().split())

# 최대 공약수
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소 공배수

for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break


# 유클리드 호제법 사용
def GCD(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def LCM(a, b):
    lcm = (a * b) // GCD(a, b)
    return lcm


print(GCD(a, b))
print(LCM(a, b))
