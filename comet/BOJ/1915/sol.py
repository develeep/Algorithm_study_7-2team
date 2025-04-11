import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 532ms
## 공간복잡도 : 57280kb
def find(width, length, arr):
    max_val = -9999
    for i in range(1, width):
        for j in range(1, length):
            if arr[i][j] and arr[i-1][j-1] and arr[i][j-1] and arr[i-1][j]:
                arr[i][j] += min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1])


    for i in arr:
        max_val = max(max_val, max(i))
    return max_val ** 2




width, length = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(width)]
print(find(width, length, arr))