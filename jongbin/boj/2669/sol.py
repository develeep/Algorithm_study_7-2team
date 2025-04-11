n = 4
zero_list = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(n):
    x1,y1,x2,y2 = map(int,(input().split()))

    for n in range(y1,y2):
        for m in range(x1,x2):
            zero_list[n][m] = 1

for i in range(100):
    for j in range(100):
        if zero_list[i][j] == 1:
            cnt += 1
print(cnt)