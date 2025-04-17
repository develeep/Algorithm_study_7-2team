from collections import deque
import math
inf = math.inf
n = int(input())
graph = {}
ans_lst = []  # 회장 후보들
ans = inf   #회장 후보 점수
while True:
    a, b = map(int, input().split())
    if a < 0 and b < 0:
        break
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

def bfs(i):
    q = deque()
    q.append(i)
    visited = [0] * (n+1)
    visited[i] = 1
    max_val = 0 #친구 사이의 거리
    while q:
        node = q.popleft()
        max_val = visited[node] # 마지막에 들어가는 값이 제일 큼
        for next_n in graph.get(node,[]):
            if not visited[next_n]: #방문 안했으면
                q.append(next_n)
                visited[next_n] = visited[node] + 1

    return max_val - 1

for i in range(1, n+1):
    dis = bfs(i)    #i의 점수
    if ans > dis:   #회장 후
        ans = dis
        ans_lst = []
        ans_lst.append(i)
    elif ans == dis:
        ans_lst.append(i)

print(ans, len(ans_lst))
print(' '.join(map(str, ans_lst)))