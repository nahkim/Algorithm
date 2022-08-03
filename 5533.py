# from pprint import pprint
# import sys

# sys.stdin = open('input.txt', 'r')
n = int(input())
res = [0 for _ in range(n)]

matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)

# 총 3게임
for k in range(3):
    for i in range(n):
        for j in range(n):
            check = matrix[i][k]
            if i == j:
                continue
            if matrix[i][k] == matrix[j][k]:
                check = 0
                break
        res[i] += check

for score in res:
    print(score)