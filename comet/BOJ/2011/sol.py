import sys
sys.stdin = open("input.txt", "r")
#############################################

def find(code):
    if code[1] == 0:
        return 0
    dp = [0] * (len(code))
    dp[0] = 1
    dp[1] = 1


    for i in range(2, len(code)):
        if code[i] == code[i - 1] == 0:
            return 0
        if code[i]:
            dp[i] += dp[i - 1]
        if code[i - 1] and code[i - 1] * 10 + code[i] <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000

    return dp[-1]
code = [0] + list(map(int, list(input().strip())))
print(find(code))