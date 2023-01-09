# 완전 탐색(brute forcing)
# 가능한 경우의 수를 모두 검사해보는 탐색 방법


n = int(input())    # n시 59분 59초까지

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)

