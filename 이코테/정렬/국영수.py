# 백준 10825번 문제






"""
N = int(input())

stu = []
for _ in range(N):
    input_data = input().split()
    stu.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

stu = sorted(stu, key=lambda score: score[1], reverse=True)

for score in stu:
    print(score[0])


12
Junkyu 50 60 100
Sankeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""
