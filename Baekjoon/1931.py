import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    arr.append([s, e])


# arr.sort(key = lambda x: (x[1], x[0]))    # 아래와 같음
arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

last_time = 0
cnt = 0

for i in range(n):
    if arr[i][0] >= last_time:
        cnt += 1
        last_time = arr[i][1]
print(cnt)