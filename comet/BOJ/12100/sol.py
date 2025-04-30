import sys
sys.stdin = open('input.txt', 'r')
#################################
## 시간 복잡도 : 132ms
## 공간 복잡도 : 32412kb
def check_max(arr):
    global length, max_val
    for i in range(length):
        for j in range(length):
            max_val = max(max_val, arr[i][j])

def shift(arr, direc):
    global length
    visited = [[0] * length for _ in range(length)]
    if direc == 1:
        for j in range(length):
            pointer = 0
            for i in range(length):
                if not arr[i][j]:
                    continue
                temp = arr[i][j]
                arr[i][j] = 0
                arr[pointer][j] = temp
                if pointer != 0 and arr[pointer][j] == arr[pointer - 1][j] and not visited[pointer - 1][j]:
                    arr[pointer - 1][j] += arr[pointer][j]
                    arr[pointer][j] = 0
                    visited[pointer - 1][j] = 1
                else:
                    pointer += 1
    elif direc == 2:
        for i in range(length):
            pointer = length - 1
            for j in range(length - 1, -1, -1):
                if not arr[i][j]:
                    continue
                temp = arr[i][j]
                arr[i][j] = 0
                arr[i][pointer] = temp
                if pointer != length - 1 and arr[i][pointer] == arr[i][pointer + 1] and not visited[i][pointer + 1]:
                    arr[i][pointer + 1] += arr[i][pointer]
                    arr[i][pointer] = 0
                    visited[i][pointer + 1] = 1
                else:
                    pointer -= 1
    elif direc == 3:
        for j in range(length):
            pointer = length - 1
            for i in range(length - 1, -1, -1):
                if not arr[i][j]:
                    continue
                temp = arr[i][j]
                arr[i][j] = 0
                arr[pointer][j] = temp
                if pointer != length - 1 and arr[pointer][j] == arr[pointer + 1][j] and not visited[pointer + 1][j]:
                    arr[pointer + 1][j] += arr[pointer][j]
                    arr[pointer][j] = 0
                    visited[pointer + 1][j] = 1
                else:
                    pointer -= 1
    elif direc == 4:
        for i in range(length):
            pointer = 0
            for j in range(length):
                if not arr[i][j]:
                    continue
                temp = arr[i][j]
                arr[i][j] = 0
                arr[i][pointer] = temp
                if pointer != 0 and arr[i][pointer] == arr[i][pointer - 1] and not visited[i][pointer - 1]:
                    arr[i][pointer - 1] += arr[i][pointer]
                    arr[i][pointer] = 0
                    visited[i][pointer - 1] = 1
                else:
                    pointer += 1

    return arr


def dfs(arr, cnt):

    if cnt == 5:
        check_max(arr)
        return
    for direc in range(1, 5):
        temp_arr = [idx[:] for idx in arr]
        dfs(shift(temp_arr, direc), cnt + 1)


length = int(input())
arr = [list(map(int, input().split())) for _ in range(length)]
max_val = 0
dfs(arr, 0)
print(max_val)