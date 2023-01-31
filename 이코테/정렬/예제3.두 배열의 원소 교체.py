n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    A.sort()
    B.sort()
    A[0], B[-1] = B[-1], A[0]

print(A)
print(B)
print(sum(A))
