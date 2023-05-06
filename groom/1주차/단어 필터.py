s_len, e_len = map(int, input().split())
s = input()
e = input()

res = ''
i = 0
while i <= e_len - s_len:
	if e[i:i + s_len] == s:
		i += s_len
	else:
		res += e[i]
		i += 1

while i < e_len:
	res += e[i]
	i += 1

if res == '':
	print('EMPTY')
else:
	print(res)

# res = e.replace(s, '')
# if res == '':
# 	print("EMPTY")
# else:
# 	print(res)