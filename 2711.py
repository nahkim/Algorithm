T = int(input())

for test_case in range(T):
    num, word = input().split()
    num = int(num)
    print(word[0:num - 1], end='')
    print(word[num:])