import sys
sys.stdin = open("input.txt", 'r')

def check_candy(candy):
    max_count = 0
    for i in range(N):
        count = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
    return max_count

def check_candy2(candy):
    max_count = 0
    for j in range(N):
        count = 1
        for i in range(N-1):
            if candy[i][j] == candy[i+1][j]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
    return max_count



N = int(input())
candies = [list(map(str, input().strip())) for _ in range(N)]
result1 = 0
result2 = 0
result = 0
for i in range(N):
    for j in range(N):
        if i + 1 < N:
            if candies[i][j] != candies[i+1][j]:
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                result1 = check_candy(candies)
                result2 = check_candy2(candies)
                result = max(result, result1, result2)
                candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]

        if j + 1 < N:
            if candies[i][j] != candies[i][j+1]:
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                result1 = check_candy(candies)
                result2 = check_candy2(candies)
                result = max(result, result1, result2)
                candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]


print(result)



