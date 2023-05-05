formula1, formula2 = input().split()

res1 = eval(formula1)
res2 = eval(formula2)

if res1 < res2:
	print(res2)
else:
	print(res1)