import sys 
sys.stdin = open('C:/Users/namja/OneDrive/Desktop/gitProject/Algorithm_study_7-2team/ImSeoHyun/BOJ/1764/input.txt', 'r')

n, m = map(int, input().split())

unHear = []
for _ in range(n):
    unHear.append(input().strip())

unSee = []
for _ in range(m):
    unSee.add(input().strip())

result = []
for name in unHear:
    if name in unSee:
        result.append(name)

result.sort()

print(len(result))
for p in result:
    print(p)
