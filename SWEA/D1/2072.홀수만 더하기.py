
n = int(input())


for i in range(n):

    arr = list(map(int, input().split()))
    result = 0

    for num in arr:
        if num % 2:
            result += num

    print(f"#{i+1} {result}")