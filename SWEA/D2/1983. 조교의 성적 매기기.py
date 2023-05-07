import sys

sys.stdin = open("input.txt", "r")

t = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, t + 1):

    n, k = map(int, input().split())
    stu = []

    for idx in range(n):
        mid, final, assign = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (assign * 0.2)
        stu.append(total)

    k_score = stu[k - 1]  # k번째 학생의 점수

    stu.sort(reverse=True)
    div = n // 10  # n / 10명의 학생에게 동일한 평점 부여 가능   ex) n = 40이면 4명씩 동일한 평점
    k_idx = stu.index(k_score) // div  # 동일한 평점을 가진 인원의 비율로 나눔  ex) 4로 나눔

    print(f"#{i} {score[k_idx]}")
