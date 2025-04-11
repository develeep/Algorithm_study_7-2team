'''
문제 )
하위 7명의 성적을 점수가 낮은 순으로 각 줄마다 출력한다.
하위 7명의 성적의 커트라인에 동점자가 있을 경우에도 7명만 출력함녀된다.
성적은 소수점 단위까지 간다.

입력값>
n = 개수
score = 점수 배열

배열 순회 하면서
오름차순 정렬
7명만 출력
'''
import sys

n = int(sys.stdin.readline())
score = [float(sys.stdin.readline().rstrip()) for i in range(n)]

score.sort(reverse=False)
for i in range(7):
    print(f"{score[i]:.3f}")
