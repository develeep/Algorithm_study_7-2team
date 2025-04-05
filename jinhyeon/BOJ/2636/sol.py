def back(top, result, pre_num = 0, pre_top = 0):
    if len(top[2]) == k:
        global min_cnt
        global ans
        if min_cnt > len(result):
            min_cnt = len(result)
            ans = result[:]
        return
    for i in range(3):
        if top[i]:
            num = top[i][-1]
            for j in range(3):
                if i == j or (len(top[j]) and num > top[j][-1]):
                    continue
                if num == pre_num and pre_top == j:
                    continue
                top[i].pop()
                top[j].append(num)
                result.append((i, j))
                back(top, result, num, i)
                top[i].append(num)
                top[j].pop()
                result.pop()

k = int(input())
ans = []
result = []
top = [[] for _ in range(3)]
top[0] = list(range(k, 0, -1))
min_cnt = float('inf')
back(top, ans)

print(len(result))
