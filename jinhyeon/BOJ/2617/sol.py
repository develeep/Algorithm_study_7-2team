from collections import deque
n, m = map(int, input().split())
graph = {}
b_cnt = [0] * (n+1) #0번 인덱스보다 큰 인덱스의 개수
s_cnt = [0] * (n+1) #0번 인덱스보다 작은 인덱스의 개
def bfs(i):
    visited = [0] * (n+1)
    # 방향성이 있는 그래프지만 간선의 개수를 보면 visited배열을 사용해야
    q = deque()
    q.append(i)
    visited[i] = 1
    cnt = 0
    while q:
        node = q.popleft()
        for next_node in graph.get(node,[]):
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = 1
                b_cnt[next_node] += 1   # next_node 입장에서는 i가 더 크기 때문
                cnt += 1    #i번 인덱스보다 작은 인덱스의 개수

    s_cnt[i] = cnt

for _ in range(m):
    a, b = map(int, input().split())
    graph.setdefault(a, []).append(b)

for i in range(1, n+1):
    bfs(i)
num = n // 2
ans = 0
for i in range(1, n+1):
    if s_cnt[i] > num or b_cnt[i] > num:
        ans += 1
print(ans)