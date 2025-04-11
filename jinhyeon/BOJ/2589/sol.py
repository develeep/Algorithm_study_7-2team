from collections import deque
r, c = map(int, input().split())

dxl = [0, 1, 0, -1]
dyl = [1, 0, -1, 0]
arr = [input() for _ in range(r)]

def bfs(x, y):
    visited = [[0] * c for _ in range(r)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    max_dis = 0
    while q:
        x, y = q.popleft()
        max_dis = visited[x][y]
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if (
                    0 <= nx < r and 0 <= ny < c
                    and arr[nx][ny] == 'L'
                    and not visited[nx][ny]
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return max_dis - 1
max_dis = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            max_dis = max(max_dis, bfs(i, j))
print(max_dis)