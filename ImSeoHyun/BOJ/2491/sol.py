n = int(input())
arr = list(map(int, input().split()))

inc = dec = maxL = 1

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        inc += 1
    else:
        inc = 1

    if arr[i] <= arr[i - 1]:
        dec += 1
    else:
        dec = 1

    maxL = max(maxL, inc, dec)

print(maxL)