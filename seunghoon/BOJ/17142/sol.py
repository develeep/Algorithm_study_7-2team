import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = ((0,-1),(0,1),(1,0),(-1,0))
def bfs(active_arr):
  que = deque()
  visited = [[0]*n for _ in range(n)]
  for ax,ay in active_arr:
    que.append((ax,ay,0))
    visited[ax][ay] = 1
  cnt = len(birus)
  res_depth = 0
  while que:
    x,y,depth = que.popleft()
    for dx,dy in dxy:
      nx,ny = x+dx, y+dy
      if not(0<=nx<n and 0<=ny<n):
        continue
      if visited[nx][ny] or grid[nx][ny]==1:
        continue
      if grid[nx][ny] == 0:
        res_depth = max(depth +1, res_depth)
        cnt += 1
      visited[nx][ny] = 1
      que.append((nx,ny,depth+1))
  
  return (cnt, res_depth)

def dfs(i, active_arr):
  global res
  if len(active_arr) == m:
    cnt, depth = bfs(active_arr)
    if cnt == blank:
      res = min(res, depth)
    return
  for idx in range(i,len(birus)):
    dfs(idx+1, active_arr + [birus[idx]])


n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

birus = []
blank = 0
res = 100000000000000000000
for i in range(n):
  for j in range(n):
    if grid[i][j] == 2:
      birus.append((i,j))
      blank += 1
    if grid[i][j] == 0:
      blank += 1  
dfs(0, [])
print(res if res < 100000000000000000000 else -1)