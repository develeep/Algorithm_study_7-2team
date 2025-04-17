N = int(input())
top_and_bottom = [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1]]
dices = [list(map(int, input().split())) for _ in range(N)]
res = float('-inf')
for i in range(6):
    sides = 0
    std = dices[0][i]
    for j in range(N):
        ind = dices[j].index(std)
        if ind > 2:
            d_ind = 0 if ind == 5 else (1 if ind == 3 else 2)
            std = dices[j][d_ind]
        else:
            d_ind = ind
            std = dices[j][5 if ind == 0 else (3 if ind == 1 else 4)]
        sides += max([dices[j][k] for k in range(6) if top_and_bottom[d_ind][k]])
    res = max(res, sides)
print(res)

'''
# 초기 코드
N = int(input())
top_and_bottom = [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1]]
dices = [list(map(int, input().split())) for _ in range(N)]
res = float('-inf')
for i in range(6):
    sides = 0
    std = dices[0][i]
    if i > 2:
        b_ind = 0 if i == 5 else (1 if i == 3 else 2)
    else:
        b_ind = i
    sides += max([dices[0][k] for k in range(6) if top_and_bottom[b_ind][k]])
    for j in range(1, N):
        ind = dices[j].index(std)
        if ind > 2:
            d_ind = 0 if ind == 5 else (1 if ind == 3 else 2)
            std = dices[j][d_ind]
        else:
            d_ind = ind
            std = dices[j][5 if ind == 0 else (3 if ind == 1 else 4)]
        sides += max([dices[j][k] for k in range(6) if top_and_bottom[d_ind][k]])
    res = max(res, sides)
print(res)
'''