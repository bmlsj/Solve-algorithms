
n = int(input())
numlist = [str(i) for i in range(1, n+1)]
gugu = ['3', '6', '9']

for idx in range(len(numlist)):
    num = numlist[idx]
    cnt = 0

    for n in num:   # 3, 6, 9가 포함되어 있는 횟수
        if n in gugu:
            cnt += 1

    if cnt == 1:   # 박수 한번 칠 때
        numlist[idx] = '-'
    elif cnt == 2:  # 박수 두번 칠 때
        numlist[idx] = '--'

print(*numlist)