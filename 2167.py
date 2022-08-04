# pypy3로 제출해야함 아니면 시간초과

# import sys

# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)
test_case = int(input())
for _ in range(test_case):
    res = 0
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    for k in range(i, x):
        for r in range(j, y):
            res += matrix[k][r]
    # while i <= x:
    #     while j <= y:
    #         res += matrix[i][j]
    #         j += 1
    #     i += 1
    #     j = 0
    print(res)