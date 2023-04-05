n = int(input())

card = []
for _ in range(n):
    card.append(int(input()))
card.sort()

ans = 0
for i in range(len(card)-2):
    ans += (card[i] + card[i+1])
    print(ans)
    ans += card[i+2] + ans
    print(ans)

print(ans)


print((10+30)+(40+60) +(100+80))