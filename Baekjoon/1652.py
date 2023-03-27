import sys

# sys.stdin = open('input.txt', 'r')
n = int(input())

matrix = [list(input()) for _ in range(n)]
row_res = [0 for _ in range(n)]
col_res = [0 for _ in range(n)]

for i in range(n):
    row_count = 0
    col_count = 0
    for j in range(n):
        if matrix[i][j] == '.':     # 가로
            row_count += 1
        else:
            if row_count > 1:
                row_res[i] += 1
            row_count = 0
        
        if matrix[j][i] == '.':     # 세로
            col_count += 1
        else:
            if col_count > 1:
                col_res[i] += 1
            col_count = 0
    if row_count > 1:
        row_res[i] += 1
    if col_count > 1:
        col_res[i] += 1

# print(row_res, col_res)
print(sum(row_res), sum(col_res))