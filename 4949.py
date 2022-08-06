# import sys

# sys.stdin = open('input.txt', 'r')

while True:
    s = input()
    if s == '.':
        break
    check = 0
    stack1 = []
    for i in s:
        if i == '(':
            stack1.append(i)
        elif i == ')':
            if len(stack1) == 0 or stack1.pop() != '(':
                print('no')
                check = 1
                break
        
        if i == '[':
            stack1.append(i)
        elif i == ']':
            if len(stack1) == 0 or stack1.pop() != '[':
                print('no')
                check = 1
                break

    if check == 0:
        if len(stack1) == 0 and len(stack1) == 0:
            print('yes')
        else:
            print('no')