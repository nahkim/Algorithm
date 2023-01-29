import sys

n = int(sys.stdin.readline())

A_arr = list(map(int, sys.stdin.readline().split()))
B_arr = list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(n):
    min_n = min(A_arr)
    max_n = max(B_arr)

    total += min_n * max_n

    A_arr.remove(min_n)
    B_arr.remove(max_n)

print(total)