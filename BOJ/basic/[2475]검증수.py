
# arr = list(map(int, input().split()))
# ans = 0
# for i in arr:
#     ans += (i * i)
#
# print(ans % 10)

def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n-1) * n

a, b = map(int, input().split())
ans = int(fac(a) / (fac(b) * fac(a-b)))

print(ans)