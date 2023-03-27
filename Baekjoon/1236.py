from pprint import pprint

n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]
# print(matrix)
res = []
a = [0 for _ in range(n)]
b = [0 for _ in range(m)]
res.append(a)
res.append(b)
# pprint(res)

for i in range(n):
    j = 0
    while j < m:
        if matrix[i][j] == 'X':
            res[0][i] = 1
            res[1][j] = 1
        j += 1

# pprint(res)
count = m + n
count -= sum(res[0]) + sum(res[1])
count -= min(n - sum(res[0]), m - sum(res[1]))
print(count)