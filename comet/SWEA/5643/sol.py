import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 921ms
## 공간복잡도 : 92288kb
def dfs(idx):
    global up, num, down, result
    sum_val = 0
    visit = [0] * (num + 1)
    visit[idx] = 1
    cnt = 0

    stack = [idx]
    while stack:
        current = stack.pop()

        for i in up[current]:
            if not visit[i]:
                stack.append(i)
                visit[i] = 1
                cnt += 1

    stack = [idx]
    while stack:
        current = stack.pop()

        for i in down[current]:
            if not visit[i]:
                stack.append(i)
                visit[i] = 1
                cnt += 1
    if cnt == num - 1:
        result += 1

T = int(input())
for tc in range(1, T+1):
    num = int(input().strip())
    compare = int(input().strip())
    up = {}
    down = {}
    result = 0
    for i in range(1, num + 1):
        up[i] = []
        down[i] = []
    for _ in range(compare):
        a, b = map(int, input().split())        # a < b
        up[a].append(b)
        down[b].append(a)


    for i in range(1, num + 1):
        dfs(i)
    print(f'#{tc} {result}')