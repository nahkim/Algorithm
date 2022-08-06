taebo = input()

right_res = 0
left_res = 0
check = 0
for i in taebo:
    if i == '@' and check == 0:
        left_res += 1
    elif i == '(':
        check = 1
    elif i == '@' and check == 1:
        right_res += 1
print(left_res, right_res)