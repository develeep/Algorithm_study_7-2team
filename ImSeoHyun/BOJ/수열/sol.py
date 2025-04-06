n, k = map(int, input().split())
arr = list(map(int, input().split()))

sumDay = sum(arr[:k])
maxSum = sumDay

for i in range(k, n):
    sumDay = sumDay - arr[i - k] + arr[i]
    maxSum = max(maxSum, sumDay)

print(maxSum)