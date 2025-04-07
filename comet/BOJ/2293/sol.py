import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 104ms
## 공간복잡도 : 33432kb

def find(num, target):

    dp = [0] * (target + 1)

    for money in coin:
        dp[money] += 1
        for i in range(money, target + 1):
            if dp[i - money]:
                dp[i] += dp[i - money]
    return dp[target]




num, target = map(int, input().split())
coin = []
for _ in range(num):
    c = int(input())
    if c <= target:
        coin.append(c)
coin.sort()
print(find(num, target))