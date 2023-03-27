num = int(input())

for i in range(1, num + 1):
    for j in range(i, num):
        print(' ', end='')
    for k in range(1, i):
        print('*', end='')
    print('*')