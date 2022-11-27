person = 0
ans = []

for _ in range(1, 11):
    down, up = list(map(int, input().split()))
    person += (up - down)
    ans.append(person)

print(max(ans))
# or
ans.sort()
print(ans[-1])