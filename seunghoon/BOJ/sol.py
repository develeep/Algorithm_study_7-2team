from collections import deque
import sys
input = sys.stdin.readline
def return_home():
    q = deque([(0,x)])
    home_way[x] = 0
    while q:
        m, student = q.popleft()
        for way, time in students[student]:
            move = m + time
            if home_way[way] > move:
                home_way[way] = move
                q.append((move, way))

def go_party():
    q = deque([(0,x)])
    party_way[x] = 0
    while q:
        m, student = q.popleft()
        for way, time in students_reverse[student]:
            move = m + time
            if party_way[way] > move:
                party_way[way] = move
                q.append((move, way))

n,m,x = map(int,input().split())
students = [[] for _ in range(n+1)]
students_reverse = [[] for _ in range(n+1)]
home_way = [10000000000]*(n+1)
party_way = [1000000000]*(n+1)
for _ in range(m):
    start,end,t = map(int,input().split())
    students[start].append([end,t])
    students_reverse[end].append([start,t])

res = 0
return_home()
go_party()
for i in range(1, n+1):
    res = max(res, party_way[i] + home_way[i])
print(res)
