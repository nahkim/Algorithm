import sys

n = int(sys.stdin.readline())

list_ = list(map(int, sys.stdin.readline().split()))

x = int(sys.stdin.readline())

list_.sort()

start, end = 0, len(list_) - 1
tmp = []
res = 0

while start < end:
    if x < list_[start] + list_[end]:
        end -= 1
    else:
        if x == list_[start] + list_[end]:
            res += 1
        start += 1

print(res)
