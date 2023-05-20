import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ants, aphids = [], []

for i in range(n):
	ground = list(map(int, input().split()))
	for j in range(n):
		if ground[j] == 1:
			ants.append([i, j])
		elif ground[j] == 2:
			aphids.append([i, j])

ants_len = len(ants)
for y1, x1 in ants:
	min_dist = 9 ** 9
	for y2, x2 in aphids:
		dist = abs(y2 - y1) + abs(x2 - x1)
		min_dist = min(min_dist, dist)
	if min_dist > m:
		ants_len -= 1
print(ants_len)