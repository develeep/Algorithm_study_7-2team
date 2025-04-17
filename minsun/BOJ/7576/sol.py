import sys
sys.stdin = open("input.txt", "r")


from collections import deque
dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]
def tomatoma():
    global day
    while queue:
        x, y, day = queue.popleft()

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                    queue.append((nx, ny, day + 1))
                    tomatoes[nx][ny] = 1


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
day = 0
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j, day))

tomatoma()


for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            day = -1
            break

print(day)

