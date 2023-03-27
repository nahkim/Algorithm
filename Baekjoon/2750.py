n = int(input())
res = list(int(input()) for _ in range(n))
# print(res)
res.sort()
for i in res:
    print(i)