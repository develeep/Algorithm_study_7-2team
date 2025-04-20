import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

def find_treasure(start_x, start_y, cnt):
    global result
    queue = deque()
    visited = [[0] * width for _ in range(height)]
    queue.append((start_x, start_y, cnt))
    visited[start_x][start_y] = 1

    while queue:
        x, y, cnt = queue.popleft()
        result = max(result, cnt)
        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = dy + y

            if 0 <= nx < height and 0 <= ny < width:
                if treasure_map[nx][ny] == 'L' and visited[nx][ny] != 1:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

height, width = map(int, input().split())
treasure_map = [list(map(str, input().strip())) for _ in range(height)]

result = 0

for i in range(height):
    for j in range(width):
        if treasure_map[i][j] == 'L':
            find_treasure(i, j, 0)

print(result)


