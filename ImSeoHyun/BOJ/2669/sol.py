arr = [list(map(int , input().split())) for _ in range(4)]


area = [[0] * 101 for _ in range(101)]

for i in range(4):
    x1, y1, x2, y2 = arr[i]
    for x in range(x1, x2):
        for y in range(y1, y2):
            area[x][y] = 1

result = 0
for k in range(101):
    for j in range(101):
       if area[k][j] == 1:
           result += 1
print(result)
