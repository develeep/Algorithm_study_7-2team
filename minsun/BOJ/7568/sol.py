import sys
sys.stdin = open("input.txt", "r")
N = int(input()) # 사람의 수

people = []
result = []
for i in range(N):
    a, b = map(int, input().split())
    people.append((a, b))


for i in range(N):
    cnt = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt+=1
    result.append(cnt)

print(*result)

