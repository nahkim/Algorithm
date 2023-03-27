matrix = list(map(int, input().split()))

# print(matrix)

def min_list(matrix):
    res_min = []
    for num in matrix:
        i = 0
        change_num = 0
        while num:
            num, mod = divmod(num, 10)
            if (mod == 6):
                change_num += 5 * (10 ** i)
            else:
                change_num += mod * (10 ** i)
            i += 1
        res_min.append(change_num)
    return res_min

def max_list(matrix):
    res_max = []
    for num in matrix:
        i = 0
        change_num = 0
        while num:
            num, mod = divmod(num, 10)
            if (mod == 5):
                change_num += 6 * (10 ** i)
            else:
                change_num += mod * (10 ** i)
            i += 1
        res_max.append(change_num)
    return res_max

res_min = min_list(matrix)
res_max = max_list(matrix)
res_sum = 0
for num in res_min:
    res_sum += num
print(res_sum, end=' ')

res_sum = 0
for num in res_max:
    res_sum += num
print(res_sum)