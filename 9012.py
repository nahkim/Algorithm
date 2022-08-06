T = int(input())

for i in range(T):
    test_case = list(input())
    stack = []
    if len(test_case) % 2 == 1:
        print('NO')
        continue
    for j in test_case:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if len(stack)  == 0:
            print('YES')
        else:
            print('NO')