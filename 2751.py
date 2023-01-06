import sys

n = int(sys.stdin.readline())

list_ = [int(sys.stdin.readline()) for i in range(n)]

list_.sort()

for i in list_:
    print(i)
