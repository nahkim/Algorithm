import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
count = 0

for i in range(n):
    arr.append(int(sys.stdin.readline()))

while k != 0:
    # k를 주어진 동전으로 나눈 몫이 0보다 클 경우
    if k // arr[n - 1] > 0:
        count += k // arr[n - 1]    # 그 몫을 count함
        k = k % arr[n - 1]
    n -= 1
print(count)