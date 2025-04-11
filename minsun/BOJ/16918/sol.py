import sys
sys.stdin = open("input.txt", "r")

"""
RxC 직사각형 격자판 위
3초가 지난 후 폭발
폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴 빈칸이 되며, 인접한 네 칸도 파괴

"""
def boom():
    result_map = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if boom_map[i][j] == 'O':
                result_map[i][j] = '.'

                for dx, dy in dxy:
                    nx = i + dx
                    ny = j + dy

                    if 0 <= nx < R and 0 <= ny < C:
                        result_map[nx][ny] = '.'
    return result_map

dxy = [[1,0], [-1, 0], [0, 1], [0, -1]]

R,C,N = map(int, input().split())
boom_map = [list(input().strip()) for _ in range(R)]
result_map = [[0]*C for _ in range(R)]
time = 1

if N % 2 != 0:
    N -= 1
    while N > 0:
        result = boom()
        N -= 1
        if N == 0:
            break

    for i in result:
        print(*i, sep='')


else:
    for i in result_map:
        print(*i, sep='')





