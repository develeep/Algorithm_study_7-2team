n = int(input())
total = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
result = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j and total[i][0] < total[j][0] and total[i][1] < total[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)