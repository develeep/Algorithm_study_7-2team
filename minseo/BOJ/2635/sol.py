'''
>문제
다음과 같은 규칙에 따라 수를 만드려고 한다.
1. 첫번째 수로 양의 정수가 주어진다.
2. 두번째 수는 양의 정수 중에서 하나를 선택한다.
3. 세번째부터 이후에 나오는 모든 수는 앞의앞의 수(2칸 앞) - 앞의 수(1칸앞)수를 뺏거 만든다. 예를 들어,
세번째 수는 첫번째 수에서 두번째 수를 뺀 것이다.
4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
예시1)]
100 50 50 0
100 51 49 2 47
100 52

100 60 40 20 0 20 (음의 정수를 버리고 멈춤)-20 =>6
100 62 38 25 14 10 4 6 (음의 정수를 버리고 멈춤)-2 => 8

> 입력값

> 구해야 하는것
최대로 구할 수 있는 개수
최대로 구할 수 있는 경우의 수를 space로 구분하여 출력
첫번째 수 = n
두번째 수 = n // 2
- 재귄감...
def 함수(n1):
    if n1 - n2 < 0:
        리턴 n3

0 보다 클 때만 while 문
    변수1 = 첫번째 수 - 두번째 수 한 값
    변수1을 배열에 저장
    만약에 변수1이 음수라면 변수에 저장하면 안됨
    첫번째수 = 두번째 수
    두번째 수 = 변수1

0 보다 작은 경우에 while문 탈출
# n2 = n1//2
# arr = [n1,n2]
# while 0 <= n1:
#     n3 = n1 - n2
#     if n3 < 0 or 0 > n1:
#         break
#     arr.append(n3)
#     n1,n2 = n2,n3
# print(arr,len(arr))

'''
import sys

n = int(sys.stdin.readline())

def recursion(n1,n2,arr):
    n3 = n1-n2
    if n3 < 0:
        return arr
    arr += [n3]
    return recursion(n2, n3, arr)

maxlen = 0
maxarr = []
for i in range(1,n+1):
    arr = [n, i]

    curarr = recursion(n,i,arr)

    if curarr is not None:
        curlen = len(curarr)
        if curlen > maxlen:
            maxlen = curlen
            maxarr = curarr

print(maxlen)
print(*maxarr,end=' ')
