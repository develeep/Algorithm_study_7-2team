import sys
sys.stdin = open('input.txt', 'r')

arr = input()
find_str = input()

index = 0
cnt = 0
for i in range(len(arr)):
    if index > i:
        continue
    if find_str == arr[i:i+len(find_str)]:
        cnt += 1
        index = i + len(find_str)


print(cnt)