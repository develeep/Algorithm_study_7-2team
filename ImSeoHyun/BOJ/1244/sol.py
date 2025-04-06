n = int(input())  
switch = [0] + list(map(int, input().split())) 
stNum = int(input())

for _ in range(stNum):
    gender, num = map(int, input().split())

    if gender == 1:  
        for i in range(num, n+1, num):
            switch[i] = 1 - switch[i] 

    elif gender == 2: 
        switch[num] = 1 - switch[num]
        offset = 1
        while num - offset > 0 and num + offset <= n:
            if switch[num - offset] == switch[num + offset]:
                switch[num - offset] = 1 - switch[num - offset]
                switch[num + offset] = 1 - switch[num + offset]
                offset += 1
            else:
                break

# 출력 (한 줄에 20개씩)
for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
