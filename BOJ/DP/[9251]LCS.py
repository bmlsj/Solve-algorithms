import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

LCS = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

## dp 사용
"""
cache = [0] * len(str2)
for i in range(len(str1)):
    cnt = 0
    for j in range(len(str2)):
        if cnt < cache[j]:
            cnt = cache[j]

        elif str1[i] == str2[j]:
            cache[j] = cnt + 1

print(max(cache))
"""

## LCS 알고리즘
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(max(map(max, LCS)))
