from collections import deque
arr = [[i for i in input()] for _ in range(12)]
dxl = [0, 1, -1, 0]
dyl = [1, 0, 0, -1]
ans = 0


def bfs(x, y):
    q = deque()
    puyo = set()
    q.append((x, y, arr[x][y]))
    while q:
        x, y, c = q.popleft()
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 \
                    and arr[nx][ny] == c and (nx, ny) not in puyo:
                q.append((nx, ny, arr[nx][ny]))
                puyo.add((nx, ny))
    if len(puyo) >= 4:
        for x, y in puyo:
            arr[x][y] = '.'
        return True
    return False

def down():
    for i in range(6):
        for j in range(11, -1, -1):  # 빈칸이 아니면
            if arr[j][i] != '.':
                for k in range(11, j, -1):
                    if arr[k][i] == '.':
                        arr[j][i], arr[k][i] = '.', arr[j][i]
                        break

while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.':
                continue
            flag = True if bfs(i, j) else flag
    if not flag:
        break
    else:
        ans += 1
    down()
print(ans)
