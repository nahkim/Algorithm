import sys
input = sys.stdin.readline

n = int(input())
user_input = input()

res = ''
i = 0
# for i in range(0, n, 2):
while i < n:
	c = user_input[i]
	cnt = int(user_input[i + 1])
	cnt = cnt ** 2
	change_c = (ord(c) + cnt - ord('a')) % 26 + ord('a')
	res += chr(change_c)
	i += 2
print(res)