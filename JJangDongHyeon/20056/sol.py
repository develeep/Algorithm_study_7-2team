from collections import defaultdict

# 방향 벡터
# 0~7: 12시, 1시, 3시, 5시, 6시, 7시, 9시, 11시
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 입력 처리
n, M, k = map(int, input().split())
fire_ball_arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(M):
    r, c, jilyiang, sokryiock, banghyang = map(int, input().split())
    fire_ball_arr[r - 1][c - 1].append((jilyiang, sokryiock, banghyang))

# k번 이동
for _ in range(k):
    new_arr = [[[] for _ in range(n)] for _ in range(n)]

    # 1단계: 이동
    for i in range(n):
        for j in range(n):
            for jilyiang, sokryiock, banghyang in fire_ball_arr[i][j]:
                ni = (i + dx[banghyang] * sokryiock) % n
                nj = (j + dy[banghyang] * sokryiock) % n
                new_arr[ni][nj].append((jilyiang, sokryiock, banghyang))

    # 2단계: 합체 후 분열
    for i in range(n):
        for j in range(n):
            if len(new_arr[i][j]) >= 2:
                total_jilyiang = sum(f[0] for f in new_arr[i][j])
                total_sokryiock = sum(f[1] for f in new_arr[i][j])
                count = len(new_arr[i][j])
                new_jilyiang = total_jilyiang // 5
                if new_jilyiang == 0:
                    new_arr[i][j] = []
                    continue
                new_sokryiock = total_sokryiock // count
                directions = [f[2] % 2 for f in new_arr[i][j]]
                if all(d == 0 for d in directions) or all(d == 1 for d in directions):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]
                new_arr[i][j] = [(new_jilyiang, new_sokryiock, d) for d in new_dirs]

    fire_ball_arr = new_arr

# 결과 계산
result = 0
for i in range(n):
    for j in range(n):
        for jilyiang, _, _ in fire_ball_arr[i][j]:
            result += jilyiang
print(result)
