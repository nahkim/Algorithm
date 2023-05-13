import sys
input = sys.stdin.readline

n = int(input())
user_input = input()

res = ''
i = 0
while i < n:
	c = user_input[i]
	cnt = int(user_input[i + 1])
	cnt = cnt ** 2
	change_c = ord(c) + cnt
	if change_c > ord('z'):
		change_c -= ord('z')
		change_c += ord('a') - 1
	res += chr(change_c)
	i += 2
print(res)