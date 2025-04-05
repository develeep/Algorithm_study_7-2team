bingo = [list(map(int, input().split())) for _ in range(5)]
call_in = [list(map(int, input().split())) for _ in range(5)]
call = []
for i in range(5):
    call.extend(call_in[i])
check = [[0]*5 for _ in range(5)]
check_90 = [[0]*5 for _ in range(5)]
cnt = 0
for c in call:
    cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == c:
                check[i][j] = True
                check_90[j][i] = True
    if cnt <= 11:
        continue
    res, cross_l, cross_r = 0, 0, 0
    for k in range(5):
        if False not in check[k]:
            res += 1
        if False not in check_90[k]:
            res += 1
        if check[k][k]:
            cross_r += 1
        if check[k][5-k-1]:
            cross_l += 1
    if cross_l // 5 + cross_r // 5 + res >= 3:
        print(cnt)
        break