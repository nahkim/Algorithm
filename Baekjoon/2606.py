from pprint import pprint

def DFS(v):
    visited[v] = True
    for n in graph[v]:
        if visited[n] == False:
            DFS(n)

# 인접 행렬
pc_count = int(input())
graph = [[] for _ in range(pc_count + 1)]
# pprint(graph)
n = int(input())
visited = [False] * (pc_count + 1)
for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
DFS(1)
print(sum(visited) - 1)