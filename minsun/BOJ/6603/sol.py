import sys
sys.stdin = open('input.txt', 'r')
def lotto(idx, k):
    if k == 6: # k ㄱㅏ 6이 되면 끝
        print(*result)
        return

    for i in range(idx, K):
        if not visited[i]:
            result[k] = S[i]
            visited[i] = 1
            lotto(i + 1, k + 1)
            visited[i] = 0


while True:
    numbers = list(map(int, input().split()))
    K, S = numbers[0], numbers[1:]
    if numbers[0] == 0:
        break


    result = [0]*6
    visited = [0]*K

    lotto(0, 0)
    print()

