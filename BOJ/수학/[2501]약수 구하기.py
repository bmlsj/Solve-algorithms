n, k = map(int, input().split())
ans = []

for i in range(1, n+1):
    if n % i == 0:
        ans.append(i)

ans.sort()  # 이미 값은 sort 되어 있으므로 굳이 필요x

if len(ans) < k:
    print(0)
else:
    print(ans[k-1])