N, M, K = map(int, input().split())
from collections import deque

B = [[deque() for _ in range(N)] for _ in range(N)]
F = deque()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    B[r-1][c-1].append([m, s, d])
    F.append((r-1, c-1))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    new_B = [[deque() for _ in range(N)] for _ in range(N)]
    new_F = set()  # 중복 제거용

    while F:
        x, y = F.popleft()
        while B[x][y]:
            m, s, d = B[x][y].popleft()
            nx = (x + dx[d] * s) % N
            ny = (y + dy[d] * s) % N
            new_B[nx][ny].append([m, s, d])
            new_F.add((nx, ny))

    F = deque()
    for x, y in new_F:
        if len(new_B[x][y]) == 1:
            F.append((x, y))
            continue

        total_m, total_s = 0, 0
        odd, even = 0, 0
        for m, s, d in new_B[x][y]:
            total_m += m
            total_s += s
            if d % 2 == 0:
                even += 1
            else:
                odd += 1

        cnt = len(new_B[x][y])
        if total_m // 5 == 0:
            new_B[x][y] = deque()
            continue

        avg_m = total_m // 5
        avg_s = total_s // cnt
        if odd == 0 or even == 0:
            dirs = [0, 2, 4, 6]
        else:
            dirs = [1, 3, 5, 7]

        new_B[x][y] = deque()
        for d in dirs:
            new_B[x][y].append([avg_m, avg_s, d])
            F.append((x, y))

    B = new_B

# 질량 총합
ans = 0
for i in range(N):
    for j in range(N):
        for m, _, _ in B[i][j]:
            ans += m

print(ans)
