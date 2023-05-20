import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stack = []

for _ in range(n):
	command = list(input().split())
	if command[0] == 'push':
		if len(stack) == k:
			print('Overflow')
		else:
			stack.append(command[1])
	else:
		if len(stack) == 0:
			print('Underflow')
		else:
			print(stack.pop())