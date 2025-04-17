import sys
sys.stdin = open('input.txt', 'r')

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
find_N = int(input())

matrix = [[0]*N for _ in range(N)]

i, j, cnt, dr = 0, 0, N*N, 0
matrix[i][j] = cnt
cnt -= 1

while True:
    nx = i + dx[dr]
    ny = j + dy[dr]

    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0:
        i, j = nx, ny
        matrix[i][j] = cnt
        cnt -= 1
    else:
        dr = (dr+1)%4

    if cnt == 0:
        break

for i in range(N):
    for j in range(N):
        if matrix[i][j] == find_N:
            x, y = i + 1, j + 1

for l in matrix:
    print(*l)

print(x, y)