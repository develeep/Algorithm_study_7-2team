import sys

n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
# 현재 가리키는 방향을 저장하는 리스트
direction=[[1,0],[0,-1],[-1,0],[0,1]]
current_direct = 0
x,y = 0,0
visited = [(x,y)]
for m in range(len(arr)):
    if arr[m] == 'L':
        # 런타임 에러면 인덱스 문제일 가능성이 있다.
        current_direct = (current_direct - 1) % 4
    if arr[m] == 'R':
        current_direct = (current_direct + 1) % 4
    if arr[m] == 'F':
        #현재 위치 좌표 변경(이부분에서 많이 헤맸다 )
        dx,dy = direction[current_direct]
        x += dx
        y += dy
        #좌표 저장 리스트에 넣기
        visited.append((x,y))
# 좌표 저장 리스트를 순회하며
# ( 오른쪽이나 최대횟수 - 최소횟수 ) * (왼쪽의 최대 횟수 - 최소횟수) = 배열크기구하기

row = [p[0] for p in visited]
max_x =  max(row)
min_x = min(row)

col = [p[1] for p in visited]
max_y = max(col)
min_y = min(col)
# 어디가 x이고 어디가 y값인지 잘 봐야 한다. 
height = max_x - min_x + 1
width = max_y - min_y + 1

# 배열 '#'으로 초기화 하기
result = [['#'] * width for _ in range(height)]
# 위치 저장한 값만 '.'로 변경해 출력
for vx,vy in visited:
    #가장 왼쪽으로 간 좌표를 기준으로, 전체를 오른쪽으로 옮겨야 한다.
    result[vx - min_x][vy - min_y] = '.'

for r in result:
    print(''.join(r))




