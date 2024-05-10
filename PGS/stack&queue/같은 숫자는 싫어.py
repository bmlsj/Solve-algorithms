
def solution(arr):
    stack = [arr[0]]
    for i in range(1, len(arr)):

        if arr[i] == arr[i - 1]:
            continue
        stack.append(arr[i])

    return stack


def solution(s):
    # 함수를 완성하세요
    a = [s[0]]

    for i in s:
        if a[-1] == i:
            continue
        a.append(i)
    return a