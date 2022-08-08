t = int(input())
for _ in range(t):
    count = 0
    n, m = map(int, input().split())
    for num in range(n, m + 1):
        string_num = str(num)
        # count += string_num.count('0')    # 아랫줄 대신 사용가능
        for i in string_num:
            if i == '0':
                count += 1
    print(count)