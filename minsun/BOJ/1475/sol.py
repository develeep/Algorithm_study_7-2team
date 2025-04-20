import sys
sys.stdin = open('input.txt', 'r')


N = input()
counting = [0] * 10

for i in N:
    if i == '6' or i == '9':
        if counting[6] <= counting[9]:
            counting[6] += 1
        else:
            counting[9] += 1

    else:
        counting[int(i)] +=1

print(max(counting))




