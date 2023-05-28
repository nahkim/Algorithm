
N, M = map(int, input().split())
sand = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    info = list(map(int, input().split()))
    for j in range(M):
        sand[i][j] = info[j]
        
checked = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(cur):
    cy, cx = cur
    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if checked[ny][nx] or not sand[ny][nx]:
            continue
        checked[ny][nx] = 1
        DFS([ny, nx])

day = 0
while 1:
    island = 0
    for i in range(N):
        for j in range(M):
            if checked[i][j] or not sand[i][j]:
                continue
            checked[i][j] = 1
            island += 1
            DFS([i, j])

    if island > 1:
        print(day)
        break

    if island == 0:
        print(-1)
        break
    
    for i in range(N):
        for j in range(M):
            checked[i][j] = 0
    day += 1