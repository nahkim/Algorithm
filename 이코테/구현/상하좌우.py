import sys

n = int(input())

x, y = 1, 1
plans = list(map(str, sys.stdin.readline().split()))

# 방법 1
for r in plans:
    if r == "L":
        if y - 1 >= 1:
            y -= 1
    elif r == "R":
        if y + 1 <= n:
            y += 1
    elif r == "U":
        if x - 1 >= 1:
            x -= 1
    else:
        if x + 1 <= n:
            x += 1
print(x, y)

# 방법 2
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)