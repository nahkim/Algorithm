list_ = [list(input()) for _ in range(5)]
count = []
for l in list_:
    count.append(len(l))

res = ['' for _ in range(max(count))]
for w in list_:
    for i in range(len(w)):
        res[i] += w[i]
# print(res)
for w in res:
    print(w, end='')