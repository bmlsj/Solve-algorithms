n = input()
c = []
for i in n:
    c.append(i)

c.sort()

num, cnt = 0, 0
for i in c:
    if not 65 <= ord(i) <= 90:
        num += int(i)
        cnt += 1

print(''.join(c[cnt:]) + str(num))
