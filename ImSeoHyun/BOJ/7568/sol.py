import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(int , input().split())) for _ in range(n)]

res = []
cnt = 1 # 등수는 1번 부터 
isStarat = False
for i in range(n):
    if isStarat: 
        res.append(cnt) 
    cnt = 1
    for j in range(n): 
      isStarat = True
      if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
         cnt += 1 # 덩치 크면 추가 
res.append(cnt) # 포문 탈출 후 마지막 인덱스의 값 넣어주기 

print(' '.join(str(k) for k in res))