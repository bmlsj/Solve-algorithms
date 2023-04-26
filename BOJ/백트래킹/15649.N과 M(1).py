n, m = map(int, input().split())
arr = [0] * (n + 1)  # 수열을 기록할 리스트
visited = [False] * (n + 1)

def func(k):      # 현재 k개까지 수를 선택함

    if k == m:    # m개까지 모두 선택한 경우
        for i in range(m):
            print(arr[i], end=' ')  # arr에 기록한 수를 모두 출력
        print()

    for i in range(1, n + 1):    # 1부터 n개까지의 수에 대해
        if not visited[i]:       # i에 방문하지 않았다면
            arr[k] = i           # k번째 수를 i로 결정
            visited[i] = True    # i를 방문했다고 표시
            func(k + 1)          # 다음 수를 정하러 +1 해줌
            visited[i] = False   # k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니 i를 다시 방문할 수 있게 변경

# 함수 출력
func(0)
