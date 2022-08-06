n = int(input())
str_num = []

for i in range(1, 1 + n):
	str_num.append(i)

while len(str_num) > 1:
	print(str_num.pop(0), end=' ')
	str_num.append(str_num.pop(0))
print(str_num[0])
