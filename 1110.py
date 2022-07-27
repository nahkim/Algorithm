num = int(input())

res = -1
count = 0

while num != res:
    if (res == -1):
        res = num
    units = res % 10
    tens = res // 10
    res = units + tens
    res = res % 10
    res += units * 10
    count += 1
print(count)