# n이 1이 될때까지 아래 반복
# 1. n-1
# 2. n // k (n%k==0일때만)

n, k = map(int, input().split())
cnt = 0

while n > 1:
    if n % k != 0:
        n -= 1
        cnt += 1

    elif n % k == 0:
            n //= k
            cnt += 1
print(cnt)
