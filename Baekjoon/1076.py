elect = []
color = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,  'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

for _ in range(3):
	elect.append(input())
num = 0
for i in range(3):
	v = color[elect[i]]
	if i == 0:
		num += v * 10
	elif i == 1:
		num += v
	else:
		num *= 10 ** v
print(num)
