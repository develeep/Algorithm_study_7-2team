import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 188ms
## 공간복잡도 : 56604kb
def find():
    first = '.' + input().strip()
    second = '.' + input().strip()
    if len(first) < len(second):
        first, second = second, first
    dp = [[0] * (len(second)) for _ in range(len(first))]

    for i in range(1, len(first)):
        temp = dp[i - 1][0]
        for j in range(1, len(second)):
            if first[i] == second[j]:
                dp[i][j] = temp + 1

            else:
                dp[i][j] = dp[i - 1][j]
            temp = max(temp, dp[i - 1][j])
    return max(dp[-1])




print(find())