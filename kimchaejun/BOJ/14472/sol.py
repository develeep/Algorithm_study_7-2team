def check(x, y, r):
    global res
    dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    ch = []
    for dx, dy in dxy:
        cnt = 1
        for k in range(1, r):
            nx, ny = x + dx * k, y + dy * k
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == '.':
                cnt += 1
        ch.append(cnt)
    res += ch.count(L)


N, M, L = map(int, input().split())
field = [input() for _ in range(N)]
visited = [[[False]*M for _ in range(N)] for _ in range(4)]
res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == '#':
            continue
        check(i, j, L)
print(res//2)
