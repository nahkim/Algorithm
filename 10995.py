num = int(input())

for i in range(1, num + 1):
    if (i % 2 == 0):
        print(' ', end='')
    for j in range(num):
        print('*', end=' ')
    print()