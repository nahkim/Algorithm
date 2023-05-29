from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)

cnt = 9**9
D = [9**9 for _ in range(N + 1)]
D[K] = 0
Que = deque()
Que.append(K)

while Que:
	cur = Que.popleft()
	for next in graph[cur]:
		if next == K:
			cnt = min(cnt, D[cur] + 1)
		if D[next] <= D[cur] + 1:
			continue
		D[next] = D[cur] + 1
		Que.append(next)

if cnt == 9**9:
	print(-1)
else:
	print(cnt)