
t = int(input())

for i in range(1, t+1):

    arr = list(map(int, input().split()))
    arr = sorted(arr)
    arr = arr[1:-1]
    print(arr)
    print(f"#{i} {round(sum(arr) / 8)}")