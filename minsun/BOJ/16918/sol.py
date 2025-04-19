import sys
sys.stdin = open("input.txt", "r")

"""
RxC 직사각형 격자판 위
3초가 지난 후 폭발
폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴 빈칸이 되며, 인접한 네 칸도 파괴

"""
def boom(b_map):
    result_map = [['O']*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if b_map[i][j] == 'O':
                result_map[i][j] = '.'
                for dx, dy in dxy:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        result_map[nx][ny] = '.'
    return result_map

dxy = [[1,0], [-1, 0], [0, 1], [0, -1]]

R, C, N = map(int, input().split())
boom_map = [list(input().strip()) for _ in range(R)]

if N == 1:
    for i in boom_map:
        print(*i, sep='')
elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    second = boom(boom_map)
    third = boom(second)
    if N % 4 == 3:
        for i in second:
            print(*i, sep='')
    else:
        for i in third:
           print(*i, sep='')






