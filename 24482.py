import sys

sys.setrecursionlimit(10**6)

def DFS(r, depth):
    visited[r] = depth

    for i in graph[r]:
        if visited[i] == -1:
            DFS(i, depth + 1)
    return

input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [-1] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for g in graph:
    g.sort(reverse=True)

DFS(r, 0)

for i in range(1, n + 1):
    print(visited[i])