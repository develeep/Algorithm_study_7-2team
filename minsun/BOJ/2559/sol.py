import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = []
result.append(sum(arr[:K]))
for i in range(N-K):
    result.append(result[i] - arr[i] + arr[K+i])

print(max(result))