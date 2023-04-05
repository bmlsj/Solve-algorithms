# 공포도가 x인 모헙가 -> 반드시 x명 이상인 그룹에 참여
# 모든 모험가가 그룹에 들어갈 필요 없음
# 최대 만들 수 있는 그룹 수

n = int(input())  # 모험가 수
scary = list(map(int, input().split()))

scary.sort()        # 1 2 2 2 3
group = 0
k = 1

for i in range(len(scary)):
    if scary[i] <= k:
        group += 1
        k = scary[i+1]


print(group)
