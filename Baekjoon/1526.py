n = int(input())

res = 4
while res <= n:
    check = 0
    s_n = str(n)
    for i in range(len(s_n)):
        if s_n[i] == '4' or s_n[i] == '7':
            continue
        else:
            n -= 1
            check = 1
            break
    if check == 0:
        print(n)
        break
