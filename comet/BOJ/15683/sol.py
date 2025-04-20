import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 152ms
## 공간복잡도 : 32412kb

def find(y, x, cnt):
    global width, length, arr, cctv
    for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
        temp = set()
        for i in range(10):
            temp_y = y + dy * i
            temp_x = x + dx * i
            if 0 <= temp_y < width and 0 <= temp_x < length and arr[temp_y][temp_x] != 6:
                temp.add((temp_y, temp_x))
            else:
                break
        cctv[cnt].append(temp)

def dfs(idx, sett):
    global cnt, cctv
    if idx == cnt:
        global min_val, all_blank
        min_val = min(min_val, all_blank - len(sett))
        return
    if kind[idx] == 1:
        temp_set = sett | cctv[idx][0]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][1]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][2]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][3]
        dfs(idx + 1, temp_set)
    elif kind[idx] == 2:
        temp_set = sett | cctv[idx][0] | cctv[idx][2]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][1] | cctv[idx][3]
        dfs(idx + 1, temp_set)

    elif kind[idx] == 3:
        temp_set = sett | cctv[idx][0] | cctv[idx][1]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][1] | cctv[idx][2]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][2] | cctv[idx][3]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][3] | cctv[idx][0]
        dfs(idx + 1, temp_set)
    elif kind[idx] == 4:
        temp_set = sett | cctv[idx][0] | cctv[idx][1] | cctv[idx][2]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][1] | cctv[idx][2] | cctv[idx][3]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][2] | cctv[idx][3] | cctv[idx][0]
        dfs(idx + 1, temp_set)
        temp_set = sett | cctv[idx][3] | cctv[idx][1] | cctv[idx][0]
        dfs(idx + 1, temp_set)

    else:
        temp_set = sett | cctv[idx][0] | cctv[idx][1] | cctv[idx][2] | cctv[idx][3]
        dfs(idx + 1, temp_set)



width, length = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(width)]
cctv = []
cnt = 0
wall = 0
kind = []
min_val = 999999

for i in range(width):
    for j in range(length):
        if 1 <= arr[i][j] <= 5:
            cctv.append([])
            find(i, j, cnt)
            cnt += 1
            kind.append(arr[i][j])
        elif arr[i][j] == 6:
            wall += 1
all_blank = width * length - wall
dfs(0, set())
print(min_val)
