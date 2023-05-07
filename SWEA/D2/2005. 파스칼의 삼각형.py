t = int(input())

for i in range(1, t + 1):

    n = int(input())  # 파스칼 삼각형 크기
    arr = [[0] * n for _ in range(n)]   # nxn 크기 리스트
    arr[0][0] = 1

    for j in range(n):
        for k in range(n):
            if j == 0 and k == 0:
                continue
            if j - 1 >= 0 and k - 1 >= 0 and arr[j - 1][k - 1]:  # 자신의 왼쪽 위
                arr[j][k] += arr[j - 1][k - 1]

            if j - 1 >= 0 and arr[j - 1][k]:  # 자신의 오른쪽 위
                arr[j][k] += arr[j - 1][k]

    print(f"#{i}")
    for ar in arr:
        for a in ar:
            if a:
                print(a, end=' ')

        print()
