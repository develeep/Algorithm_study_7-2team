'''

재귀나 dfs
재귀로 접근할 경우
> 입력을 배열로 받기
배열 요소순회
- 점점 커지거나 같은 경우

- 점점 작아지는 경우

'''
import sys

arrlen = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

rowarr = [1]*arrlen
colarr = [1]*arrlen
biggercnt = 1
for idx in range(arrlen-1):
    if idx + 1 < arrlen:
        if arr[idx] <= arr[idx+1]:
            rowarr[idx+1] += rowarr[idx]
        if arr[idx+1] <= arr[idx]:
            colarr[idx+1] += colarr[idx]
maxrow = max(rowarr)
maxcol = max(colarr)
result = max(maxrow,maxcol)
print(result)