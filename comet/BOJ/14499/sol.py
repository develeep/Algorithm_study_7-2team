import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 40ms
## 공간복잡도 : 32544kb
def roll(dice, direc):
    if direc == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direc == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direc == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif direc == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    return




width, length, dice_y, dice_x, command_num = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(width)]
commands = list(map(int, input().split()))
dice = [0] * 7
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
for command in commands:
    if not 0 <= dice_y + dy[command] < width or not 0 <= dice_x + dx[command] < length:
        continue

    roll(dice, command)
    dice_y += dy[command]
    dice_x += dx[command]
    if not arr[dice_y][dice_x]:
        arr[dice_y][dice_x] = dice[6]
    else:
        dice[6] = arr[dice_y][dice_x]
        arr[dice_y][dice_x] = 0
    print(dice[1])