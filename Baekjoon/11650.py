import sys

n = int(sys.stdin.readline())

list_ = []

for i in range(n):
    list_.append(tuple(map(int, sys.stdin.readline().split())))

list_.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(list_[i][0], list_[i][1])
