# pypy3로 제출해야 시간초과가 안남
import sys

n, m  = map(int, sys.stdin.readline().split())

check = 0
for _ in range(m):
    if check:
        break
    k = int(input())
    list_ = list(map(int, sys.stdin.readline().split()))
    for i in range(k - 1):
        if list_[i] > list_[i + 1]:
            continue
        else:
            check = 1
            break
if check:
    print('No')
else:
    print('Yes')

# 방법 2
# import sys

# n, m  = map(int, sys.stdin.readline().split())

# check = 0
# for _ in range(m):
#     if check:
#         break
#     k = int(input())
#     list_ = list(map(int, sys.stdin.readline().split()))
#     reverse_list = list_[::]
#     reverse_list.sort(reverse=True)
#     if list_ != reverse_list:
#         check = 1
#         break
# if check:
#     print('No')
# else:
#     print('Yes')