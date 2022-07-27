import sys

sys.stdin = open("input.txt", "r")

test_case = int(input())

x_list = []
y_list = []
res = [0 for i in range(test_case)]
# print(res)
rank = 1

for i in range(test_case):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

while sum(x_list) != -test_case:
    max_x = max(x_list)
    max_y = max(y_list)
    found_x = x_list.index(max_x)
    found_y = y_list.index(max_y)
    if found_x == found_y:
        res[found_x] = rank
        rank += 1
        x_list[found_x] = -1
        y_list[found_y] = -1
    else:
        for i in range(test_case):
            if y_list[i] > y_list[found_x] or x_list[i] > x_list[found_y]:
                res[i] = rank
                x_list[i] = -1
                y_list[i] = -1
            elif y_list[i] == y_list[found_x] or x_list[i] == x_list[found_y]:
                res[i] = rank
                x_list[i] = -1
                y_list[i] = -1
        rank += 1
print(res)