import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 468ms
## 공간복잡도 : 32412kb
def b_dfs(cnt, bishop):
    if cnt == len(black):
        global b_result
        b_result = max(b_result, bishop)
        return
    y, x = black[cnt]

    if not left_right[y - x] and not right_left[y + x]:
        left_right[y - x] = 1
        right_left[y + x] = 1
        b_dfs(cnt + 1, bishop + 1)
        left_right[y - x] = 0
        right_left[y + x] = 0
    b_dfs(cnt + 1, bishop)
def w_dfs(cnt, bishop):
    if cnt == len(white):
        global w_result
        w_result = max(w_result, bishop)
        return
    y, x = white[cnt]

    if not left_right[y - x] and not right_left[y + x]:
        left_right[y - x] = 1
        right_left[y + x] = 1
        w_dfs(cnt + 1, bishop + 1)
        left_right[y - x] = 0
        right_left[y + x] = 0
    w_dfs(cnt + 1, bishop)

length = int(input())
arr = [list(map(int, input().split())) for _ in range(length)]

limit = 0

left_right = [0] * (length * 2 - 1)
right_left = [0] * (length * 2 - 1)
# 좌하향 = y + x, 우하향 = y - x
b_result = 0
w_result = 0
black = []
white = []
for i in range(length):
    for j in range(length):
        if arr[i][j]:
            if i % 2 == 0:
                if j % 2 == 0:
                    black.append((i, j))
                else:
                    white.append((i, j))
            else:
                if j % 2 == 0:
                    white.append((i, j))
                else:
                    black.append((i, j))
b_dfs(0, 0)
w_dfs(0, 0)
print(b_result + w_result)