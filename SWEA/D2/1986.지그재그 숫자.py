
t = int(input())

for i in range(1, t+1):

    n = int(input())
    ans = 0

    for num in range(1, n+1):
        if num % 2:
            ans += num
        else:
            ans -= num

    print(f"#{i} {ans}")