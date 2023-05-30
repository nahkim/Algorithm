import sys
input = sys.stdin.readline

N, M = map(int, input().split())

events = {}
for i in range(1, N + 1):
	events[i] = 0

for _ in range(M):
	event = list(map(int, input().split()))
	for i in range(1, event[0] + 1):
		tmp = event[i]
		events[tmp] += 1

max_n = 0
for k, v in events.items():
	if max_n <= v:
		max_n = v

res = []
for k, v in events.items():
	if max_n == v:
		res.append(k)

res.sort(reverse = True)
for n in res:
	print(n, end=' ')


# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# cnt = defaultdict(int)
# for _ in range(M):
#     events = list(map(int, input().split()))
#     for e in events[1:]:
#         cnt[e] += 1

# ans = []
# res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
# ans.append(res[0][0])

# for i in range(1, len(res)):
#     if res[i - 1][1] != res[i][1]:
#         break
#     ans.append(res[i][0])
    
# print(*ans)