import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for a in range(1, t + 1):
    # n : 총 문제 수
    n = int(input())
    scorelist = list(map(int, input().split()))
    
    # 결과 저장할 리스트: result
    result = [0] * (sum(scorelist) + 1)
    result[0] = 1

    for score in scorelist:
        # 뒤에서 앞으로
        for i in range(len(result) - score, -1, -1):
            # result[가능한 점수]가 있다면
            if result[i]:
                # result[그 점수 + 방금 얻은 점수]에 1을 넣어준다.
                result[i + score] = 1

    print(f"#{a} {sum(result)}")
