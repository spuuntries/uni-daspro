n, _, _, _ = input().split()
inputs = []
for i in range(int(n)):
    inputs.append([int(n) for n in input().split()])

col_arr = []
row_arr = []
for i, r in enumerate(inputs):
    to_col = []
    for j, e in enumerate(r):
        if e == -1:
            to_col.append(j)
    if len(to_col) > 0:
        col_arr.append(*to_col)
        row_arr.append(i)

hit = set()
for i, r in enumerate(inputs):
    if i in row_arr:
        for t in r:
            if t > 0:
                hit.add(t)
    for j, e in enumerate(r):
        if j in col_arr and e > 0:
            hit.add(e)

[print(e) for e in sorted(hit)]
