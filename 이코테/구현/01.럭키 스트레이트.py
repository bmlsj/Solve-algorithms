
n = input()
num = []

for i in n:
    num.append(int(i))

mid = int(len(n)//2)

left = sum(num[0:mid])
right = sum(num[mid:])

if left == right:
    print("LUCKY")
else:
    print("READY")

