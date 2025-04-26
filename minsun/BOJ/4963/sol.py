import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxs = [0, 0, -1, 1, -1, -1, 1, 1]
dys= [1, -1, 0, 0, -1, 1, -1, 1]

def find_land(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y

            if 0 <= nx < h and 0 <= ny < w :
                if visited[nx][ny] != 1 and island[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


while True:
    w, h = map(int, input().split())
    island = []
    visited = [[0]* w for _ in range(h)]
    cnt = 0

    if w == 0 and h == 0:
        break

    for _ in range(h):
        island.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visited[i][j] != 1:
                find_land(i, j)
                cnt+=1

    print(cnt)