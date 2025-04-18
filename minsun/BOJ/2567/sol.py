import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
width, height= 101, 101
white =[[0] * width for _ in range(height)]

for _ in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            white[i][j] = 1

dxy = [[0, -1], [0, 1], [1, 0], [-1, 0]]
cnt = 0

for i in range(width):
    for j in range(height):
        if white[i][j] == 1:
           for dx, dy in dxy:
                ni = dx + i
                nj = dy + j
                if white[ni][nj] == 0: # 네 방향 탐색해서 0 이 있으면 둘레를 구하는 것
                    cnt +=1
print(cnt)


