n = int(input())
dict_ = {}
cnt = 0
for i in range(n):
    n, l = map(int, input().split())
    if n in dict_:
        if dict_[n] != l:
            cnt += 1
    dict_[n] = l
print(cnt)