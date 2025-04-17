import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 740ms
## 공간복잡도 : 117564kb(pypy3)
def dfs(y, x, val, cnt):
    global result, width, length, visited
    if cnt == 4:
        result = max(result, val)
        return

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        tempy = y + dy
        tempx = x + dx
        if 0 <= tempy < width and 0 <= tempx < length and not visited[tempy][tempx]:
            visited[tempy][tempx] = 1
            dfs(tempy, tempx, val + arr[tempy][tempx], cnt + 1)
            visited[tempy][tempx] = 0

def find(y, x):
    global arr, length, width
    val = []
    if y != 0:
        val.append(arr[y - 1][x])
    if y != width - 1:
        val.append(arr[y + 1][x])
    if x != 0:
        val.append(arr[y][x - 1])
    if x != length - 1:
        val.append(arr[y][x + 1])
    if len(val) <= 2:
        return None
    elif len(val) == 3:
        return sum(val) + arr[y][x]
    else:
        return sum(val) - min(val) + arr[y][x]

width, length = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(width)]
result = -9999999
visited = [[0] * length for _ in range(width)]

for i in range(width):
    for j in range(length):
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0
        temp = find(i, j)

        if temp:
            result = max(result, temp)

print(result)