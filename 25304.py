input_total = int(input())
case = int(input())
total = 0
for _ in range(case):
    price, cnt = map(int, input().split())
    total += price * cnt
if input_total == total:
    print('Yes')
else:
    print('No')