import sys
input = sys.stdin.readline

answer = input()
start = input()
check = [False] * 4
cnt = 0

for i in range(4):
	# Strike
	if answer[i] == start:
		continue

	# Fail
	elif start[i] not in answer:
		while start[i] in answer:
			start[i] = (start[i] + 1) / 10
		# Ball (move left)
		for i in range(4):
			if start[i] == answer[i]:
				check[i] == True
		
		for i in range(3):
			if check[i] == False:
				second = start[i]
				first = second
			else:
				continue

			for j in range(i + 1, 3):
				if check[j] == False:
					second = start[j]
					start[j] = first
					break
				else:
					continue
		idx = check.index(False)