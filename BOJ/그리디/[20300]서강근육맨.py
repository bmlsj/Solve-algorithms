# 운동 기구를 최대 2개까지 선택 가능
# 이전에 사용하지 않았던 기구를 선택
# 9개의 기구가 있는 경우, PT 5번을 받아도 마지막 PT에는 1개만 사용
# 한번 PT 받을 때 : 근손실 정도 <= M
# M의 최솟값을 선택

n = int(input())
muscle = list(map(int, input().split()))
muscle.sort()
ans = []

if n % 2:
    ans.append(muscle[-1])
    muscle.pop()
    for i in range(n // 2):
        ans.append(muscle[i] + muscle.pop())

    print(max(ans))

else:
    for i in range(n // 2):
        ans.append(muscle[i] + muscle.pop())

    print(max(ans))


