chess_list = list(map(int, input().split()))
res = []

for i in range(len(chess_list)):
    if i < 2:
        res.append(1 + chess_list[i] * -1)
    elif i < 5:
        res.append(2 + chess_list[i] * -1)
    elif i == 5:
        res.append(8 + chess_list[i] * -1)
for chess in res:
    print(chess, end=' ')