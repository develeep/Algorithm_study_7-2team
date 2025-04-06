import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간 복잡도 : 1072ms
## 공간 복잡도 : 116416kb
from collections import deque
def simulation(subset):
    sunsu = deque(subset)
    result = 0
    for idx in arr:
        rue = [0, 0, 0]
        out = 0
        while out < 3:
            current = sunsu.popleft()
            sunsu.append(current)
            if idx[current] == 0:
                out += 1
            elif idx[current] == 1:
                result += rue[2]
                rue[2] = rue[1]
                rue[1] = rue[0]
                rue[0] = 1
            elif idx[current] == 2:
                result += rue[2]
                result += rue[1]
                rue[2] = rue[0]
                rue[1] = 1
                rue[0] = 0
            elif idx[current] == 3:
                result += rue[2]
                result += rue[1]
                result += rue[0]
                rue[0] = rue[1] = 0
                rue[2] = 1
            else:
                result += rue[2]
                result += rue[1]
                result += rue[0]
                result += 1
                rue[0] = rue[1] = rue[2] = 0

    global point
    point = max(point, result)
    return








def combination(cnt, subset, visited):
    if cnt == 3:
        subset.append(1)
        combination(cnt + 1, subset, visited)
        subset.pop()
        return
    if cnt == num:

        simulation(subset)
        return
    for i in range(2, num + 1):
        if not visited[i]:
            visited[i] = 1
            subset.append(i)
            combination(cnt + 1, subset, visited)
            visited[i] = 0
            subset.pop()

inning = int(input().strip())
arr = [[0] + list(map(int, input().split())) for _ in range(inning)]
num = 9
visited = [0] * (num + 1)
point = 0
combination(0, [], visited)
print(point)