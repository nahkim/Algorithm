# import sys

# sys.stdin = open('input.txt', 'r')

num = int(input())

for i in range(num):
    list_ = list(map(int, input().split()))
    # print(list_)
    list_.sort()
    print(list_[7])