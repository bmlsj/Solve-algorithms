
n = int(input())

array = []
for i in range(n):
    array.append(input().split())
    array[i][1] = int(array[i][1])  # 숫자를 정수형으로 저장

for i in range(n):
    for j in range(i+1, n):
        if array[i][1] > array[j][1]:  # i 번째 이후 더 작은 값이 있으면, swap
            array[i][1], array[j][1] = array[j][1], array[i][1]
            array[i][0], array[j][0] = array[j][0], array[i][0]

for i in range(n):
    print(array[i][0], end=' ')

# -----------------------------------------
# 이코테 답안

m = int(input())
arr2 = []
for i in range(m):
    input_data = input().split()
    arr2.append( (input_data[0], int(input_data[1])) )  # 숫자를 정수로 저장

# key를 이용해, 점수를 기준으로 정렬
arr2 = sorted(arr2, key=lambda student: student[1])

for student in arr2:
    print(student[0], end=' ')


