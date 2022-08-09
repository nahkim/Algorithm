T = int(input())
res = [0, 0, 0, 0, 0]
for test_case in range(T):
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        res[4] += 1
    elif n > 0:
        if m > 0:
            # 1사분면
            res[0] += 1
        else:
            # 4사분면
            res[3] += 1
    else:
        if m > 0:
            # 2사분면
            res[1] += 1
        else:
            # 3사분면
            res[2] += 1
for i in range(4):
    print(f'Q{i + 1}: {res[i]}')
print(f'AXIS: {res[4]}')