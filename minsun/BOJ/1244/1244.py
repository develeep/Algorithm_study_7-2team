import sys
sys.stdin = open("input.txt", "r")


N = int(input())
switch = list(map(int,input().split()))

student_N = int(input())
for i in range(student_N):
    gender, switch_N = map(int, input().split())


    if gender == 1:
        for s in range(1, N + 1):
            if s % switch_N == 0:
                if switch[s-1] == 1:
                    switch[s-1] = 0
                else:
                    switch[s-1] = 1

    else:
        left = switch_N-2
        right = switch_N

        while left >= 0 and right < N:
            if switch[left] != switch[right]:
                break
            left -=1
            right +=1

        for j in range(left+1, right):
            if switch[j] == 1:
                switch[j] = 0
            else:
                switch[j] = 1

for k in range(N):
    print(switch[k], end = " ")
    if (k+1) % 20 == 0 :
        print()
