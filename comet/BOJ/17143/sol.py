import sys
sys.stdin = open("input.txt", "r")
#############################################


def catch(row, arr):
    for i in range(width):
        if arr[i][row]:
            global result
            result += shark[arr[i][row]][size]
            shark.pop(arr[i][row])
            arr[i][row] = 0
            return
    return

def move(arr):
    delete = []     # 위치 - 이동거리 // 넓이
    for i in list(shark.keys()):
        arr[shark[i][0]][shark[i][1]] = 0
        move = shark[i][speed]

        while move:
            if shark[i][direc] == 1:
                if move >= shark[i][0]:
                    move -= shark[i][0]
                    shark[i][0] = 0
                    shark[i][direc] = 2
                else:
                    shark[i][0] -= move
                    break

            elif shark[i][direc] == 2:
                if move >= width - 1 - shark[i][0]:
                    move -= width - 1 - shark[i][0]
                    shark[i][0] = width - 1
                    shark[i][direc] = 1
                else:
                    shark[i][0] += move
                    break
            elif shark[i][direc] == 4:
                if move >= shark[i][1]:
                    move -= shark[i][1]
                    shark[i][1] = 0
                    shark[i][direc] = 3
                else:
                    shark[i][1] -= move
                    break
            else:
                if move >= length - 1 - shark[i][1]:
                    move -= length - 1 - shark[i][1]
                    shark[i][1] = length - 1
                    shark[i][direc] = 4
                else:
                    shark[i][1] += move
                    break

        if arr[shark[i][0]][shark[i][1]]:
            delete.append(i)
        else:
            arr[shark[i][0]][shark[i][1]] = i

    for i in delete:
        if arr[shark[i][0]][shark[i][1]] == 0:
            arr[shark[i][0]][shark[i][1]] = i
        elif arr[shark[i][0]][shark[i][1]] != i:
            if shark[arr[shark[i][0]][shark[i][1]]][size] > shark[i][size]:
                shark.pop(i)
            else:
                shark.pop(arr[shark[i][0]][shark[i][1]])
                arr[shark[i][0]][shark[i][1]] = i

reverse = [2, 1, 4, 3]
speed = 2
direc = 3
size = 4
width, length, num = map(int, input().split())
shark = {}
arr = [[0] * length for _ in range(width)]
result = 0
# 0 : y, 1 : x, 2 : speed, 3 : direc, 4 : size
for i in range(1, num + 1):
    shark[i] = list(map(int, input().split()))
    shark[i][0] -= 1
    shark[i][1] -= 1
    arr[shark[i][0]][shark[i][1]] = i

if num != 0:
    for i in range(length):

        catch(i, arr)
        move(arr)

        if len(shark.keys()) == 0:
            break
print(result)
