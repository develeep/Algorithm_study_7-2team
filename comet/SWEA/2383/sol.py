import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 340ms
## 공간복잡도 : 70144kb
def dfs(cnt, one, two):
    if cnt == len(people):
        simulation(one, two)
        return
    one.append(cnt)
    dfs(cnt + 1, one, two)
    one.pop()
    two.append(cnt)
    dfs(cnt + 1, one, two)
    two.pop()

def simulation(one,two):
    global time, min_time, stair

    time1 = []
    time2 = []
    for i in one:
        time1.append(time[i][0])
    for i in two:
        time2.append(time[i][1])
    time1.sort(reverse=True)
    time2.sort(reverse=True)
    timer1 = 1
    wait1 = 0
    wait2 = 0
    down1 = [0] * stair[0][2]
    down2 = [0] * stair[1][2]
    while time1 or time2 or wait2 or wait1 or sum(down1) != 0 or sum(down2) != 0:
        timer1 += 1
        for i in range(len(time1) - 1, -1, -1):
            time1[i] -= 1
        for i in range(len(time1) - 1, -1, -1):
            if time1[i] == 0:
                time1.pop()
                wait1 += 1
            else:
                break
        down1.pop(0)
        temp = 3 - sum(down1)
        if wait1 > temp:
            down1.append(temp)
            wait1 -= temp
        else:
            down1.append(wait1)
            wait1 = 0

        for i in range(len(time2) - 1, -1, -1):
            time2[i] -= 1
        for i in range(len(time2) - 1, -1, -1):
            if time2[i] == 0:
                time2.pop()
                wait2 += 1
            else:
                break
        down2.pop(0)
        temp = 3 - sum(down2)
        if wait2 > temp:
            down2.append(temp)
            wait2 -= temp
        else:
            down2.append(wait2)
            wait2 = 0


    min_time = min(min_time, timer1)


T = int(input())
for tc in range(1, T+1):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(length)]
    stair = []
    people = []
    time = []
    min_time = 99999999
    for i in range(length):
        for j in range(length):
            if arr[i][j] == 1:
                people.append((i, j))
            elif arr[i][j] >= 2:
                stair.append([i, j, arr[i][j]])
    for y, x in people:
        time.append((abs(y - stair[0][0]) + abs(x - stair[0][1]), abs(y - stair[1][0]) + abs(x - stair[1][1])))


    dfs(0, [], [])
    print(f'#{tc} {min_time}')