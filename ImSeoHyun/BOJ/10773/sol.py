t = int(input())

arr = []
for _ in range(t):
    inp = int(input())
    if inp == 0: 
        arr.pop() 
    else: 
        arr.append(inp)

print(sum(arr))
