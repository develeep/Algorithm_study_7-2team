
def init_shark():
    for i in range(1, m+1):
        r, c, s, d, z = map(int,input().split())
        arr[r-1][c-1] = i
        sharks.append([s, d, z])    # 상어 정보는 0번 인덱스부터

def catch_shark(i):
    global ans
    for j in range(r):
        if arr[j][i]:
            n = arr[j][i] - 1   #상어 번호
            # print(n, sharks[n][2])
            ans += sharks[n][2]
            arr[j][i] = 0
            break
def shark_move():
    moved_sharks = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                n = arr[i][j]
                x, y = calcultae_shark_next_position(n, i, j)
                if moved_sharks[x][y]:
                    if sharks[n - 1][2] < sharks[moved_sharks[x][y] - 1][2]: #기존 상어가 크면
                        continue
                moved_sharks[x][y] = n
    for i in range(r):
        for j in range(c):
            arr[i][j] = moved_sharks[i][j]
def calcultae_shark_next_position(n, x, y):
    """
    :param n: 상어 번호
    :param x: 상어의 현재 x값
    :param y: 상어의 현재 y값
    :return:
    """
    next_x, next_y = x, y
    s, d, z = sharks[n - 1][0], sharks[n - 1][1], sharks[n - 1][2]
    if d == 1:  #상
        dis_to_wall = x
        if s > dis_to_wall:
            s -= dis_to_wall
            if ((s-1) // (r-1) + 1) % 2:    #벽 튕귄 횟수가 홀수면
                next_x = (s-1) % (r-1) + 1
                sharks[n - 1][1] = 2
            else:
                next_x = (r - 1)- ((s-1) % (r-1) + 1)
        else:
            next_x -= s

    elif d == 2:    # 하
        dis_to_wall = (r-1) - x
        if s > dis_to_wall:
            s -= dis_to_wall
            if ((s-1) // (r-1) + 1) % 2:    #벽 튕귄 횟수가 홀수면
                next_x = (r - 1) - ((s-1) % (r-1) + 1)
                sharks[n - 1][1] = 1
            else:
                next_x = (s - 1) % (r - 1) + 1
        else:
            next_x += s

    elif d == 4:    #좌
        dis_to_wall = y
        if s > dis_to_wall:
            s -= dis_to_wall
            if (((s - 1) // (c - 1)) + 1) % 2:  # 벽 튕귄 횟수가 홀수면
                next_y = (s - 1) % (c - 1) + 1
                sharks[n - 1][1] = 3
            else:
                next_y = (c - 1) - ((s - 1) % (c - 1) + 1)
        else:
            next_y -= s
    else:   # 우
        dis_to_wall = (c - 1) - y
        if s > dis_to_wall:
            s -= dis_to_wall
            if ((s - 1) // (c - 1) + 1) % 2:  # 벽 튕귄 횟수가 홀수면
                next_y = (c - 1) - ((s - 1) % (c - 1) + 1)
                sharks[n - 1][1] = 4
            else:
                next_y = (s - 1) % (c - 1) + 1
        else:
            next_y += s

    return next_x, next_y


r, c, m = map(int, input().split())
arr = [[0] * c for _ in range(r)]
sharks = [] #상어 정보를 담음  (속도, 방향, 크기)

ans = 0
init_shark()
for i in range(c):  # 0~5
    catch_shark(i)
    shark_move()
print(ans)