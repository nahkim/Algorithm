import sys
sys.setrecursionlimit(10**7)

def DFS(graph, visited, start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, visited, i)

n, m = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
graph = [[] for i in range(n + 1)]
cnt = 0

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, len(visited)):
    if visited[i] == False:
        DFS(graph, visited, i)
        cnt += 1
print(cnt)