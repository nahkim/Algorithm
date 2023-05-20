# from pprint import pprint
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, k = map(int, input().split())
ground = [([0] * n) for _ in range(n)]
# print(ground)
for i in range(k):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	ground[x][y] += 1

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >= 0 and nx < n and ny >= 0 and ny < n:
			ground[nx][ny] += 1
			# pprint(ground)

res = 0
for arr in ground:
	res += sum(arr)
print(res)
	