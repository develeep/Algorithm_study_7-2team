import sys
sys.stdin = open('input.txt', 'r')


##################################################
def fall_down():
    # 아래서부터 역방향으로 탐색
    for y in range(weight):
        for x in range(height - 1, -1, -1):
          # 값이 있으면 그 값 아래에 빈 공간이 없을때까지 값 변경 진행
            if grid[x][y] != '.':
                i = x
                while i + 1 < height:
                    if grid[i + 1][y] == '.':
                        grid[i][y], grid[i + 1][y] = grid[i + 1][y], grid[i][y]
                        i += 1
                    else:
                        break


dxy = ((1, 0), (-1, 0), (0, -1), (0, 1))
def check():
    flag = 0
    for i in range(height):
        arr = 0
        for j in range(weight):
            # 값이 있을시 인근에 같은값 탐색
            if grid[i][j] != '.':
                color = grid[i][j]
                # 찾은 값 좌표를 set에 담는다.
                arr = set()
                arr.add((i,j))

                # stack 이용 유사 bfs 진행
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < height and 0 <= ny < weight):
                            continue
                        if (nx,ny) in arr:
                            continue
                        # 같은색이면 추가
                        if grid[nx][ny] == color:
                            arr.add((nx,ny))
                            stack.append((nx, ny))
                if len(arr) >= 4:
                    flag = 1
                    for ax, ay in arr:
                        grid[ax][ay] = '.'
            else:
                if not arr:
                    break
    # 한번이라도 변경이 일어나면 1 반환
    if flag:
        return 1
    return 0


height = 12
weight = 6
grid = [[s for s in input().rstrip()] for _ in range(height)]

res = 0
# 변경이 없을때까지 반복
while 1:
    if check():
        res += 1
        fall_down()
    else:
        break
print(res)
