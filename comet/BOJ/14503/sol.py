import sys
sys.stdin = open("input.txt", "r")
#############################################


## 시간복잡도 : 36ms
## 공간 복잡도 : 32412kb

width, length = map(int, input().split())
y, x, direc = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(width)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
rotate = [3, 0, 1, 2]
visited = [[0] * length for _ in range(width)]
while 1:

    if not visited[y][x]:
        visited[y][x] = 1
        cnt += 1
    flag = 0
    for dy, dx in direction:
        temp_y = y + dy
        temp_x = x + dx
        if 0 <= temp_y < width and 0 <= temp_x < length and not room[temp_y][temp_x] and not visited[temp_y][temp_x]:
            flag = 1
    if not flag:
        y -= direction[direc][0]
        x -= direction[direc][1]
        if not (0 <= y < width and 0 <= x < length and not room[y][x]):
            break
        else:
            continue
    else:
        direc = rotate[direc]
        dy, dx = direction[direc]
        temp_y = y + dy
        temp_x = x + dx
        if 0 <= temp_y < width and 0 <= temp_x < length and not room[temp_y][temp_x] and not visited[temp_y][temp_x]:
            y += dy
            x += dx
print(cnt)