s = input()

c = []
for i in s:
    c.append(i)

mid = len(c) // 2

cnt_l = []
idx = set()
for i in range(1, mid + 1):
    cnt = 0

    for j in range(0, len(c), i):
        if c[:i] == c[j:j+i]:
            cnt += 1
            idx.add(i)
    cnt_l.append(cnt)

max_cnt = max(cnt_l)
idx_num = 0
idx_list = list(idx)
for i in range(len(cnt_l)):
    if idx_list[i] == max_cnt:
        idx_num = i
print(len(c) + idx_num - max_cnt)