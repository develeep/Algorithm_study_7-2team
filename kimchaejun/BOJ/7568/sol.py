# git config 수정
N = int(input())
weights, heights = [], []
res = [1] * N
for _ in range(N):
    w, h = map(int, input().split())
    weights.append(w)
    heights.append(h)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if weights[i] > weights[j] and heights[i] > heights[j]:
            res[j] += 1
print(*res)
