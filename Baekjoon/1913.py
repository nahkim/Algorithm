import sys
from pprint import pprint

line = int(sys.stdin.readline())
n = int(sys.stdin.readline())
tmp = line * line

res = []
for i in range(line):
    res.append([0] * line)

# print(res)

i, j = 0, 0
while line > 0:
    res[i][j] = tmp
    while i < line:
        i += 1
        tmp -= 1
        res[i][j] = tmp
    while j < line:
        j += 1
        tmp -= 1
        res[i][j] = tmp
    while i >= 0:
        i -= 1
        tmp -= 1
        res[i][j] = tmp
    line -= 1
    while j >= 0:
        j -= 1
        tmp -= 1
        res[i][j] = tmp
pprint(res)





# for i in range(line):
#     res[i][0] = tmp
#     tmp2 = tmp - line
#     for j in range(1, line):
#         res[i][j] = tmp2
#         tmp2 += 1
#     tmp -= 1
pprint(res)