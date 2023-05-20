import sys
input = sys.stdin.readline

n = int(input())
events = []
for _ in range(n):
	s, e = map(int, input().split())
	events.append([s, e])

events.sort(key = lambda x : (x[1], x[0]))
cnt = end = 0
for s, e in events:
	if s > end:
		cnt += 1
		end = e

print(cnt)