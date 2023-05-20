n = int(input())
coins = [40, 20, 10, 5, 1]
cnt = 0

for coin in coins:
	cnt += n // coin
	n %= coin
print(cnt)