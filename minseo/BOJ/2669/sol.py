'''

네개중에 가장 큰 수를 구한다. -> 이만큼의 정사각형 배열 만들기

visted 배열을 만든ㄴ다. (100*100)
반복문(4번)
    시작점(x,y) - 끝점(x,y) = 변의 길이 (a,b)
    visited배열에서 시작점 + a 만큼 반복하기
        visited 배열에서 끝점 + b 만큼 반복하기
            visited 배열 체크하기
visited배열 크기 만큼 반복
    visited 배열의 체크된 부분이 있으면 +=1
값 출력
> 입력값을 받는다.


> 정사각형이 차지하느 면적을 출력한다. (중복은 1번만)
> 소요 시간;: 1시간 24분 17초
'''
import sys

cnt = 0
visited = [[0]*100 for _ in range(100)]
for tc in range(4):
    arr = list(map(int,sys.stdin.readline().split()))
    # x의 끝점
    square_x = abs(int(arr[0] - arr[2]))
    # y의 끝점
    square_y = abs(int(arr[1] - arr[3]))

    for squere_col in range(arr[1],(arr[1]+square_y)):
        for squere_row in range(arr[0],(arr[0]+square_x)):
            visited[squere_col][squere_row] = 1

for row in range(len(visited)):
    for col in range(len(visited)):
        if visited[row][col] == 1:
            cnt+=1
print(cnt)



