N, M = map(int, input().split())
temp = list(map(int, input().split()))
f_sum = sum(temp[:M])
res = f_sum
for i in range(M, N):
    f_sum += temp[i] - temp[i-M]
    res = max(res, f_sum)
print(res)
