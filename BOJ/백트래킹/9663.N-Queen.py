import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
isused_col = [0] * (n + 1)  # 열에 대응되는 값  -> (x, y) => isused[y] = True
isused_dia1 = [0] * (2 * n)  # 왼쪽 아래에서 우측 위로 가는 대각선
isused_dia2 = [0] * (2 * n)  # 왼쪽 위에서 우측 아래로 가는 대각선


def func(curr):
    global cnt
    if curr == n:  # 퀸 n개를 놓는데 성공
        cnt += 1
        return

    # 한 행에 2개인지는 생각할 필요가 없음 -> 열과 대각선만 생각
    # 같은 열 : 같은 y를 가지는 가
    # 같은 대각선 : x + y나 x - y가 같을 때

    for i in range(n):
        if isused_col[i] or isused_dia1[i + curr] or isused_dia2[curr - i + (n - 1)]:
            continue

        isused_col[i] = True
        isused_dia1[i + curr] = True
        isused_dia2[curr - i + n - 1] = True

        func(curr + 1)
        isused_col[i] = False
        isused_dia1[i + curr] = False
        isused_dia2[curr - i + n - 1] = False


func(0)
print(cnt)