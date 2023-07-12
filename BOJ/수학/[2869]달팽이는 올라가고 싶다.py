import sys

input = sys.stdin.readline
# Ax + B(x-1) = V
A, B, V = map(int, input().split())

x = (V - B) / (A - B)

if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
