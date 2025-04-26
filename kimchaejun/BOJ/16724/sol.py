def dfs(x, y):
    global res
    visited[x][y] = 1
    dx, dy = dxy[num[field[x][y]]]
    nx, ny = x + dx, y + dy
    if not visited[nx][ny]:
        dfs(nx, ny)
    elif visited[nx][ny] == 1:
        res += 1
    visited[x][y] = 2


N, M = map(int, input().split())
field = [list(map(str, input().strip())) for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
num = {'R': 0, 'L': 1, 'D': 2, 'U': 3}
visited = [[0]*M for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
print(res)
