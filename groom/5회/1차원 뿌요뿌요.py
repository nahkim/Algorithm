import sys
input = sys.stdin.readline

n, m = map(int, input().split())
user_input = input().rstrip()
stack = []
stack.append(('', 1))

user_input += 'z'
for c in user_input:
	if stack[-1][0] != c:
		if m <= stack[-1][1]:
			top = stack[-1][0]
			while top == stack[-1][0]:
				stack.pop()
	if stack[-1][0] == c:
		stack.append((c, stack[-1][1] + 1))
	else:
		stack.append((c, 1))
stack.pop()

if len(stack) > 1:
	for c, cnt in stack:
		print(c, end='')
		
else:
	print('CLEAR!')