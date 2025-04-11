t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for i in range(n):
        num = coins[i]
        cnt = 1
        for j in range(1, m+1):
            if j >= num:
                dp[j] = dp[j] + dp[j - num]
    print(dp[m])