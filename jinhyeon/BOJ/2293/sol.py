n, k = map(int, input().split())

dp = [0] * (k + 1)
dp[0] = 1
for i in range(n):
    num = int(input())
    for j in range(1, k+1):
        if j >= num:
            dp[j] += dp[j - num]
print(dp[k])