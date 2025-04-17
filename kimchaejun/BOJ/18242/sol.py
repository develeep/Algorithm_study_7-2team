N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
matrix90 = list(map(list, zip(*matrix[::-1])))
res_dict = {0: 'UP', 1: 'DOWN', 2: 'LEFT', 3: 'RIGHT'}
up_down, left_right = [], []
for i in range(N):
    tmp = matrix[i].count('#')
    if tmp > 2:
        up_down.append(tmp)
for i in range(M):
    tmp90 = matrix90[i].count('#')
    if tmp90 > 2:
        left_right.append(tmp90)
res = up_down + left_right
print(res_dict[res.index(min(res))])
