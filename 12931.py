import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

while sum(arr) != 0:
    # 홀수일 경우 1 빼기
    for i in range(n):
        if arr[i] % 2 == 1:
            arr[i] = arr[i] - 1
            cnt += 1
    if sum(arr) == 0:
        break
    # 짝수일 경우 나누기
    for i in range(n):
        arr[i] //= 2
    cnt += 1
print(cnt)