t = int(input())

for i in range(1, t + 1):

    n = int(input())
    arr = list(map(int, input().split()))

    result = 0
    max_value = arr[-1]  # 리스트를 뒤집은 이후 가장 첫 인덱스를 max 값으로 생각

    for j in range(n - 2, -1, -1):   # 끝에서 2번째 값부터 0까지 비교
        if max_value <= arr[j]:   # max값 보다 더 크다면, 그 값을 max_value에 넣음
            max_value = arr[j]
        else:        # max값 보다 작다면, 그 차를 result에 더한다.
            result += (max_value - arr[j])

    print(f"#{i} {result}")

