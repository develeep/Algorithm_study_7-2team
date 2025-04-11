T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot_cnt = [0] * 31
    res, tmp = float('inf'), 0
    for c in carrot:
        carrot_cnt[c] += 1
    for i in range(1, 31):
        for j in range(i, 31):
            S, M, L = sum(carrot_cnt[:i]), sum(carrot_cnt[i:j]), sum(carrot_cnt[j:])
            if not (S == 0 or M == 0 or L == 0):
                tmp = max(S, M, L) - min(S, M, L)
                res = min(tmp, res)
    print(f"#{tc} {res if res != float('inf') else -1}")
