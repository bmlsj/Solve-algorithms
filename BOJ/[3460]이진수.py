t = int(input()) # 테스트 케이스 수

for _ in range(t):
    n = int(input())

    n = bin(n)   # 앞에 0b가 포함되어 나타남(문자열)
    n = n[2:]    # 13 -> 1101
                 # 최하위 비트의 위치가 0이므로 가장 왼쪽으로 바꿔준다(거꾸로 선언)

    for idx, val in enumerate(n[::-1]):
        if val == '1':
            print(idx, end=" ")

