def check():
    global cnt
    score = 0
    # 행 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if bingo[i][j] == 0:
                cnt += 1
        if cnt == 5:
            score += 1
    # 열 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if bingo[j][i] == 0:
                cnt += 1
        if cnt == 5:
            score += 1
    # 대각선 1
    cnt = 0
    for i in range(n):
        if bingo[i][i] == 0:
            cnt += 1
    if cnt == 5:
        score += 1
    # 대각선 2
    cnt = 0
    for i in range(n):
        if bingo[i][n-1-i] == 0:
            cnt += 1
    if cnt == 5:
        score += 1

    return score
n = 5
bingo = [list(map(int, input().split()))for _ in range(n)]
speak = []
for _ in range(n):
    speak += list(map(int, input().split()))
cnt = 0
for i in range(25):
    for j in range(n):
        for k in range(n):
            if speak[i] == bingo[j][k]:
                bingo[j][k] = 0
                cnt += 1
    result = check()
    if result >= 3:
        print(i+1)
        break