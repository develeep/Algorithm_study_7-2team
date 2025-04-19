import sys
sys.stdin = open('input.txt', 'r')

dxs = [0, 0, -1, 1, -1, -1, 1, 1]
dys= [1, -1, 0, 0, -1, 1, -1, 1]

N = int(input())
info = [list(map(str, input().strip())) for _ in range(N)]

cnt = 0


for i in range(N):
    for j in range(N):
        for dx, dy in zip(dxs, dys):
            word = ''
            for k in range(5):
                nx = i + dx * k
                ny = j + dy * k

                if 0 <= nx < N and 0 <= ny < N:
                    word+= info[nx][ny]
                else:
                    break
            if word == 'MOBIS':
                cnt += 1

print(cnt)



