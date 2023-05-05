import sys
sys.stdin = open("input.txt", "r")
for i in range(1, 2):

    n, pw = map(int, input().split())
    pw = str(pw)
    stack = [pw[0]]

    for j in range(1, len(pw)):
        if len(stack) and stack[-1] == pw[j]:
            stack.pop()
        else:
            stack.append(pw[j])

    print(f"#{i} {int(''.join(stack))}")
