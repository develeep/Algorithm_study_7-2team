from collections import deque
k = int(input().rstrip())
w, h = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(h)]

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

dxl = [0, 1, 0, -1]
dyl = [1, 0, -1, 0]
dxl_j = [-2, -1, 1, 2,  2,  1, -1, -2]
dyl_j = [1,  2,  2, 1, -1, -2, -2, -1]

def bfs(x, y, jump): #jump = 점프 횟수
    q = deque()
    q.append((x, y, jump))
    visited[jump][x][y] = 1
    while q:
        x, y, jump = q.popleft()
        if x == h-1 and y == w-1:
            return visited[jump][x][y] - 1
        if jump:
            for dx, dy in zip(dxl_j, dyl_j):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny] and not visited[jump-1][nx][ny]:
                    q.append((nx , ny, jump-1))
                    visited[jump-1][nx][ny] = visited[jump][x][y] + 1
        for dx, dy in zip(dxl, dyl):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny] and not visited[jump][nx][ny]:
                q.append((nx ,ny, jump))
                visited[jump][nx][ny] = visited[jump][x][y] + 1
    return -1

ans = bfs(0, 0, k)
print(ans)
