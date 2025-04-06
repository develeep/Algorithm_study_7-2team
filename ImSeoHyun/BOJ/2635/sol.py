a = int(input())
maxL = 0
result = []

for sec in range(1, a + 1):
    arr = [a, sec]
    while True:
        next = arr[-2] - arr[-1]
        if next < 0:
            break
        arr.append(next)

    if len(arr) > maxL:
        maxL = len(arr)
        result = arr

print(maxL)
print(' '.join(map(str, result)))
