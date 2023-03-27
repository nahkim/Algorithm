total_list = [[0] * 100 for _ in range(100)]
total = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            total_list[i][j] = 1

print(sum(map(sum, total_list)))