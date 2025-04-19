def is_prime_num(num):
    flag = True
    if num == 1 and num == 0:
        flag = False
    for i in range(2, num):
        if not num % i:
            flag = False
            break
    return flag

def is_beautiful_prime_num(num):
    if not is_prime_num(num):
        return
    if len(str(num)) == n:
        result.append(num)
        return

    for i in range(10):
        is_beautiful_prime_num(num * 10 + i)

result = []
n = int(input())
for i in range(2, 10):
    is_beautiful_prime_num(i)

print('\n'.join(map(str, result)))