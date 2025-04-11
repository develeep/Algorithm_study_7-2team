import sys
sys.stdin = open("input.txt", "r")
#############################################

## 시간 복잡도 : 436ms(pypy3)
## 공간 복잡도 : 129288kb
def select(arr):
    before = fireball[arr[0]][direc] % 2
    for i in arr:
        if before != fireball[i][direc] % 2:
            return False
    return True
y = 0
x = 1
mass = 2
speed = 3
direc = 4

length, num, turns = map(int, input().split())
fireball = {}
result = 0
grid = {}
div = length - 1
idx = num + 1
for i in range(length):
    for j in range(length):
        grid[(i, j)] = []
for i in range(1, num + 1):
    fireball[i] = list(map(int, input().split()))
    fireball[i][0] -= 1
    fireball[i][1] -= 1
    grid[(fireball[i][0], fireball[i][1])].append(i)



for turn in range(turns):
    temp = []
    for fire in fireball.keys():    # 파이어볼 이동

        grid[(fireball[fire][y], fireball[fire][x])].remove(fire)
        if fireball[fire][direc] == 0:
            fireball[fire][y] -= fireball[fire][speed]
            fireball[fire][y] %= length
            if fireball[fire][y] < 0:
                fireball[fire][y] += length

        elif fireball[fire][direc] == 2:
            fireball[fire][x] += fireball[fire][speed]
            fireball[fire][x] %= length

        elif fireball[fire][direc] == 4:
            fireball[fire][y] += fireball[fire][speed]
            fireball[fire][y] %= length

        elif fireball[fire][direc] == 6:
            fireball[fire][x] -= fireball[fire][speed]
            fireball[fire][x] %= length
            if fireball[fire][x] < 0:
                fireball[fire][x] += length

        elif fireball[fire][direc] == 1:
            fireball[fire][x] += fireball[fire][speed]
            fireball[fire][x] %= length

            fireball[fire][y] -= fireball[fire][speed]
            fireball[fire][y] %= length
            if fireball[fire][y] < 0:
                fireball[fire][y] += length

        elif fireball[fire][direc] == 3:
            fireball[fire][x] += fireball[fire][speed]
            fireball[fire][x] %= length

            fireball[fire][y] += fireball[fire][speed]
            fireball[fire][y] %= length

        elif fireball[fire][direc] == 5:
            fireball[fire][y] += fireball[fire][speed]
            fireball[fire][y] %= length

            fireball[fire][x] -= fireball[fire][speed]
            fireball[fire][x] %= length
            if fireball[fire][x] < 0:
                fireball[fire][x] += length

        else:
            fireball[fire][y] -= fireball[fire][speed]
            fireball[fire][y] %= length
            if fireball[fire][y] < 0:
                fireball[fire][y] += length

            fireball[fire][x] -= fireball[fire][speed]
            fireball[fire][x] %= length
            if fireball[fire][x] < 0:
                fireball[fire][x] += length
        grid[(fireball[fire][y], fireball[fire][x])].append(fire)

        if len(grid[(fireball[fire][y], fireball[fire][x])]) >= 2:
            temp.append((fireball[fire][y], fireball[fire][x]))

    temp = list(set(temp))
    for dy, dx in temp:
        if len(grid[(dy, dx)]) >= 2:
            sum_mass = 0
            sum_speed = 0
            number = len(grid[(dy, dx)])
            can = select(grid[(dy, dx)])
            for i in grid[(dy, dx)]:
                sum_mass += fireball[i][mass]
                sum_speed += fireball[i][speed]
                fireball.pop(i)
            grid[(dy, dx)].clear()
            sum_mass = sum_mass // 5

            sum_speed = sum_speed // number

            if sum_mass:
                if can:
                    for i in 0, 2, 4, 6:
                        fireball[idx] = [dy, dx, sum_mass, sum_speed, i]
                        grid[(dy, dx)].append(idx)
                        idx += 1

                else:
                    for i in 1, 3, 5, 7:
                        fireball[idx] = [dy, dx, sum_mass, sum_speed, i]
                        grid[(dy, dx)].append(idx)
                        idx += 1




for i in fireball.keys():
    result += fireball[i][mass]
print(result)