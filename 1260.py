import sys
from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m ,v = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for g in graph:
    g.sort()

DFS(graph, v, visited)
print()

visited = [False] * (n + 1)
BFS(graph, v, visited)