import sys
input = sys.stdin.readline

balance, cnt = map(int, input().split())
waiting = []

for _ in range(cnt):
	cmd = list(input().split())
	
    # deposit
	if cmd[0] == 'deposit':
		balance += int(cmd[1])
	# pay	
	elif cmd[0] == 'pay':
		if balance >= int(cmd[1]):
			balance -= int(cmd[1])
	# reservation
	else:
		waiting.append(int(cmd[1]))
	
	while len(waiting) > 0:
		if balance >= waiting[0]:
			balance -= waiting.pop(0)
		else:
			break
print(balance)