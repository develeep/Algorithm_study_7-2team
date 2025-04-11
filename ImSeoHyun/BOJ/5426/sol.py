
T = int(input())

for tc in range(T):
    arr = input()

    length = len(arr)

    i = 1
    letter = []
    while i * i < length:
        i += 1
    if i * i == length:
        idx = 0
        for m in range(i):
            row = []
            for c in range(i):
                row.append(arr[idx])
                idx += 1
            letter.append(row)

    rotateLetter = list(zip(*letter[::-1]))
    result =[]

    for q in range(i):
        for w in range(i):
            result.append(rotateLetter[q][w])

    print(''.join(result[::-1]))

                

