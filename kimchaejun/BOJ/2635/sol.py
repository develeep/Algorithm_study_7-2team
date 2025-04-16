def fibonacci(n, n2):
    global res, cnt
    tmp_fib = [n, n2]
    idx = 2
    while True:
        tmp = tmp_fib[idx-2] - tmp_fib[idx-1]
        if tmp < 0:
            fib_len = len(tmp_fib)
            if fib_len > cnt:
                res.clear()
                cnt = fib_len
                res.append(tmp_fib)
            break
        tmp_fib += [tmp]
        idx += 1


N = int(input())
res, cnt = [], 0
for i in range(N, -1, -1):
    fibonacci(N, i)
print(cnt)
print(' '.join(map(str, res[0])))