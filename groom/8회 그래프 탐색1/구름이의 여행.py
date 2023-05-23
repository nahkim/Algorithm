from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
	u, v = map(int, input().split())
	
	graph[u].append(v)
	graph[v].append(u)

distance = [ 9**9 for _ in range(n + 1)]
distance[1] = 0

que = deque()
que.append(1)

while que:
	cur = que.popleft()
	for next in graph[cur]:
		if distance[next] <= distance[cur] + 1:
			continue
		distance[next] = distance[cur] + 1
		que.append(next)
	
if distance[n] <= k:
	print("YES")
else:
	print("NO")