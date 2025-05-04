import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]
def friends(start_x, start_y):
    cnt = 0
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if matrix[nx][ny] != 'X':
                    if matrix[nx][ny] == 'P':
                        cnt += 1
                    queue.append((nx,  ny))
                    visited[nx][ny] = 1

    if cnt == 0:
        print("TT")
    else:
        print(cnt)

N, M = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'I':
            friends(i, j)