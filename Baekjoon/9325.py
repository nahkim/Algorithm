t = int(input())

for _ in range(t):
    s = int(input())
    option = int(input())
    for i in range(option):
        option_count, price = map(int, input().split())
        s += option_count * price
    print(s)