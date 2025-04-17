n = int(input())
arr = list(map(int,input().split()))
lis_arr = [arr[0]]
idx_arr = [(arr[0],0)]

def lower_bownd(x):
    left = 0
    right = len(lis_arr)
    while left < right:
        mid = (left + right) // 2
        if lis_arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return right

for i in range(1, len(arr)):
    num = arr[i]
    last_num = len(lis_arr)-1
    if lis_arr[last_num] < num:
        lis_arr.append(num)
        idx_arr.append((num, last_num + 1))
    else:
        idx = lower_bownd(num)
        lis_arr[idx] = num
        idx_arr.append((num , idx))

j = len(lis_arr)-1
result_arr = []
for i in range(len(idx_arr)-1,-1,-1):
    num, idx = idx_arr[i]
    if idx == j:
        result_arr.append(num)
        j -= 1

print(len(result_arr))
print(' '.join(map(str, result_arr[::-1])))
