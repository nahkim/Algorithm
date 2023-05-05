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
