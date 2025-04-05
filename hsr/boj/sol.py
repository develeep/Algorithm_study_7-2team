from collections import deque

ROW, COL = 12, 6


field = [list(input().strip()) for _ in range(ROW)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    queue = deque([(x, y)])
    visited[x][y] = True
    group = [(x, y)]  # 같은 색상의 뿌요 위치 저장

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < ROW and 0 <= ny < COL and not visited[nx][ny] and field[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True
                group.append((nx, ny))
    
    return group

def apply_gravity():
    for col in range(COL):
        # 현재 열에서 뿌요들을 모으고, 다시 아래부터 채우기
        stack = []
        for row in range(ROW - 1, -1, -1):
            if field[row][col] != '.':
                stack.append(field[row][col])
        
        # 다시 아래에서부터 채우기
        for row in range(ROW - 1, -1, -1):
            if stack:
                field[row][col] = stack.pop(0)
            else:
                field[row][col] = '.'

count = 0  # 연쇄 횟수

while True:
    visited = [[False] * COL for _ in range(ROW)]
    to_pop = []  # 터질 뿌요 그룹 저장

    # 터질 뿌요 찾기
    for i in range(ROW):
        for j in range(COL):
            if field[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, field[i][j])
                if len(group) >= 4:
                    to_pop.extend(group)

    #없다면 종료
    if not to_pop:
        break

    # 뿌요 터뜨리기
    for x, y in to_pop:
        field[x][y] = '.'

    # 중력 적용
    apply_gravity()

   
    count += 1

# 결과 출력
print(count)