
t = int(input())

for i in range(t):

    arr = list(map(int, input().split()))
    print(f"#{i+1} {round(sum(arr) / 10)}")