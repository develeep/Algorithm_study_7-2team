from collections import deque
def bfs(node):
    q = deque([(node, 0)])
    visited = [0] * (n+1)
    visited[node] = 1
    while q:
        student, depth = q.popleft()
        for friend in nodes[student]:
            if visited[friend]:
                continue
            visited[friend] = 1
            q.append((friend, depth+1))

    return depth


n = int(input())
nodes = [[] for _ in range(n+1)]

while 1:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break

    nodes[a].append(b)
    nodes[b].append(a)

min_depth = 100000000
res = []
for i in range(1,n+1):
    depth = bfs(i)
    if min_depth > depth:
        min_depth = depth
        res = [i]
    elif min_depth == depth:
        res.append(i)

print(min_depth, len(res))
print(' '.join(map(str, res)))