import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 64ms
## 공간복잡도 : 35004kb
from collections import deque

length = int(input())
apple_num = int(input())
arr = [[0] * length for _ in range(length)]
arr[0][0] = 1
que = deque([(0, 0)])
for _ in range(apple_num):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = 2
command_num = int(input())
command = []
for _ in range(command_num):
    time, d = input().split()
    if d == 'L':
        command.append((int(time), 0))
    else:
        command.append((int(time), 1))
direc = 1
rotate = [(3, 1), (0, 2), (1, 3), (2, 0)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
y, x = 0, 0
time = 0
pointer = 0
while 1:
    time += 1
    y += dy[direc]
    x += dx[direc]
    if not(0 <= y < length and 0 <= x < length) or arr[y][x] == 1:
        break   # 벽과 몸에 부딫히면 종료
    que.append((y, x))
    if arr[y][x] != 2:
        tempy, tempx = que.popleft()
        arr[tempy][tempx] = 0
    arr[y][x] = 1

    if pointer < command_num and time == command[pointer][0]:
        direc = rotate[direc][command[pointer][1]]
        pointer += 1
print(time)