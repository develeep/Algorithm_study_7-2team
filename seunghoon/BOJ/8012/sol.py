import sys
input = sys.stdin.readline
from collections import deque
def make_tree():
    tree[1] = [1,0]
    q = deque([(1, 0)])
    visited = [0] * (n+1)
    visited[1] = 1
    while q:
        x,depth = q.popleft()
        for node in nodes[x]:
            if visited[node]:
                continue
            visited[node] = 1
            tree[node].append(x)
            tree[node].append(depth+1)
            q.append((node, depth+1))

def get_length(a,b):
    pa,da = tree[a]
    pb,db = tree[b]

    oda = da
    odb = db

    while da != db:
        if da > db:
            a = pa
            pa, da = tree[a]
        else:
            b = pb
            pb, db = tree[b]
    while a != b:
        a = pa
        b = pb
        pa, da = tree[a]
        pb, db = tree[b]
    root_depth = da
    return oda-root_depth + odb-root_depth

n = int(input())
nodes = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

make_tree()
m = int(input())
a = int(input())
res = 0
for _ in range(m-1):
    b = int(input())
    res += get_length(a,b)
    a = b
print(res)