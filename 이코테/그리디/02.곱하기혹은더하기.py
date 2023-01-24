n = input()

n_list = []
for s in n:
    n_list.append(s)

calc = max(int(n_list[0]) + int(n_list[1]), int(n_list[0]) * int(n_list[1]))
result = 0

for i in range(2, len(n_list)):
    calc = max(calc * int(n_list[i]), calc + int(n_list[i]))

print(calc)