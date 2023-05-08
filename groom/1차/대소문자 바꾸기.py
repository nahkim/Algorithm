# 아스키 코드로 구현
user_input = int(input())
res = ''
s = input()
i = 0

while i < user_input:
	asci = ord(s[i])
	if asci >= 97 and asci <= 122:
		change_asci = asci - 32
	else:
		change_asci = asci + 32
	change_c = chr(change_asci)
	res += change_c
	i += 1
print(res)

# 내장함수로 구현1
import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
res = ''
for c in s:
	if c.islower():
		res += c.upper()
	elif c.isupper():
		res += c.lower()
print(res)

# 내장함수 구현2
import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
print(s.swapcase())