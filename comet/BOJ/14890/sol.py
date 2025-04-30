import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 40ms
## 공간복잡도 : 32412kb
def find_y(i):
    global arr
    before = arr[i][0]
    for j in range(length):
        if before == arr[i][j]:
            continue
        if before - 1 == arr[i][j]:
            if j <= length - road:
                for k in range(road):
                    if arr[i][j + k] != arr[i][j]:
                        return False
                    else:
                        len_did[i][j + k] = 1

            else:
                return False

        elif before + 1 == arr[i][j]:
            if j >= road:
                for k in range(1, road + 1):
                    if arr[i][j - k] != arr[i][j - 1] or len_did[i][j - k]:
                        return False
                    else:
                        len_did[i][j - k] = 1
            else:
                return False
        else:
            return False
        before = arr[i][j]

    return True

def find_x(j):
    global arr
    before = arr[0][j]
    for i in range(length):
        if before == arr[i][j]:
            continue
        if before - 1 == arr[i][j]:
            if i <= length - road:
                for k in range(road):
                    if arr[i + k][j] != arr[i][j]:
                        return False
                    else:
                        wid_did[i + k][j] = 1

            else:
                return False

        elif before + 1 == arr[i][j]:
            if i >= road:
                for k in range(1, road + 1):
                    if arr[i - k][j] != arr[i - 1][j] or wid_did[i - k][j]:
                        return False
                    else:
                        wid_did[i - k][j] = 1
            else:
                return False
        else:
            return False
        before = arr[i][j]

    return True

length, road = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(length)]
len_did = [[0] * length for _ in range(length)]
wid_did = [[0] * length for _ in range(length)]
cnt = 0
for i in range(length):
    if find_y(i):
        cnt += 1
    if find_x(i):
        cnt += 1
print(cnt)