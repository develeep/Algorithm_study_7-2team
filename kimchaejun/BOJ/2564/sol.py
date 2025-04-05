'''
10 5
3
1 4
3 2
2 8
2 3
첫째 수는 상점이 위치한 방향을 나타내는데,
1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고,
상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다.
상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.
-1 if 1 <= i < M and 1 <= j < N else
'''
N, M = map(int, input().split())
K = int(input())
around_len = (N+M) * 2
line = [0] * (around_len + 1)
for i in range(1, K+2):
    pos, way = map(int, input().split())
    if pos == 1:
        line[way] = i
    elif pos == 2:
        line[N+(N-way)+M] = i
    elif pos == 3:
        line[N*2+(M-way)+M] = i
    else:
        line[N+way] = i
res, tmp_len = 0, 0
s_ind = line.index(K+1)
for i in range(1, K+1):
    t_ind = line.index(i)
    if s_ind < t_ind:
        tmp_len = len(line[s_ind:t_ind])
    else:
        tmp_len = len(line[t_ind:s_ind])
    if tmp_len > around_len // 2:
        tmp_len = around_len - tmp_len
    res += tmp_len
print(res)
# dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# matrix = [[-1 if 1 <= i < M and 1 <= j < N else 0 for j in range(N+1)] for i in range(M+1)]
# sx, sy = 0, 0
# for i in range(1, K+2):
#     pos, way = map(int, input().split())
#     if pos == 1:
#         matrix[0][way] = i
#         if i == 4:
#             sx, sy = 0, way
#     elif pos == 2:
#         matrix[M][way] = i
#         if i == 4:
#             sx, sy = M, way
#     elif pos == 3:
#         matrix[way][0] = i
#         if i == 4:
#             sx, sy = way, 0
#     else:
#         matrix[way][N] = i
#         if i == 4:
#             sx, sy = way, N
# for i in range(1, K+1):
#
#
# for i in range(M+1):
#     print(*matrix[i])
