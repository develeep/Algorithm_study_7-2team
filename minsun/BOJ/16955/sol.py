import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

def check():
    global result
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 'X':
                for k in range(4):
                    nx = i
                    ny = j

                    count = 1
                    for _ in range(4):
                        nx += dx[k]
                        ny += dy[k]
                        if 0 <= nx  < N and 0 <= ny < N and pan[nx][ny] == 'X':
                            count += 1
                        else:
                            break
                    if count == 5:
                        result = 1
                        break


N = 10
pan = [list(map(str, input().strip())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if pan[i][j] == '.':
            pan[i][j] = 'X'
            check()
            pan[i][j] = '.'


print(result)

