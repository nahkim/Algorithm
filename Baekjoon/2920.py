num_list = list(map(int, input().split()))
# print(num_list)

check = 0
if num_list[0] == 1:
    count = 1
    for i in num_list:
        if i == count:
            count += 1
            continue
        else:
            check = 1
            print('mixed')
            break
    if check == 0:
        print('ascending')
        check = 1
elif num_list[0] == 8:
    count = 8
    for i in num_list:
        if i == count:
            count -= 1
            continue
        else:
            check = 1
            print('mixed')
            break
    if check == 0:
        print('descending')
        check = 1
if check == 0:
    print('mixed')
