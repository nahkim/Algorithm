import sys

n, m = map(int, sys.stdin.readline().split())
min_list = []

# 방법1
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    min_n = min(tmp)
    min_list.append(min_n)
print(max(min_list))

# 방법2
res = 0
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    min_n = min(tmp)
    res = max(res, min_n)
print(res)