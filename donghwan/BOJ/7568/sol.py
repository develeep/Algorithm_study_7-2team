import sys
sys.stdin = open('input.txt', 'r')
##################################################

"""
어떻게 풀까?
각 사람들의 덩치별로 한번씩 돌면서 전체를 비교해볼까?
그러면서 순번을 찾자

"""

T = int(input())    # Test case 개수를 받아오는 코드 # 가끔 10번 돈다고 하면 int(input())이 아니라 그냥 정수 10 적어주기
for tc in range(1, T + 1):
    N = int(input())
    human = [list(map(int, input().split())) for _ in range(N)]             # 덩치 리스트 받아옴
    result = [0] * N                                                        # 결과 저장

    for i in range(N):                                                      # 덩치 한명당 전체를 돌면서 비교
        idx = 1                                                             # 처음 시작값 1번
        for j in range(N):
            if human[i][0] < human[j][0] and human[i][1] < human[j][1]:     # 덩치가 작을 때만 후순위로 지정하면 동일한 등수는 고려 안해도됨
                idx += 1

        result[i] = idx                                                     # 결과에 넣어주기

    for p in result:
        print(p, end=" ")
    print()