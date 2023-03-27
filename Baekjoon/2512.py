import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
limit_buget = int(input())

start = 0
end  = max(arr)
while start <= end:
    mid = (start + end) // 2
    curr = 0
    for buget in arr:
        if buget >= mid:
            curr += mid
        else:
            curr += buget
    if curr <= limit_buget:
        start =  mid + 1
    else:
        end = mid - 1
print(end)