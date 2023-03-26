import sys

location = sys.stdin.readline()

col = int(ord(location[0])) - int(ord('a')) + 1
row = int(location[1])
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
cnt = 0

for step in steps:
    next_col = col + step[0]
    next_row = row + step[1]
    if next_col <= 8 and next_col >= 1 and next_row <= 8 and next_row >= 1:
        cnt += 1
print(cnt)