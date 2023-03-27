import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = int(sys.stdin.readline())

for i in range(n):
    max_num = max(arr[i: min(n, i + count + 1)])
    index = arr.index(max_num)

    for j in range(index, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
    
    count -= index - i
    if count == 0:
        break

print(*arr)