import sys
input = sys.stdin.readline

N = int(input())
temp = [list(input().split()) for _ in range(N)]
arr = [[i, *j] for i, j in  enumerate(temp)]
arr.sort(key=lambda x: (int(x[1]), x[0]))
for i in arr:
    print(i[1], i[2])