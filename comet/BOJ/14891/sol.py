import sys
sys.stdin = open('input.txt', 'r')
#######################################
## 시간 복잡도 : 36ms
## 공간 복잡도 : 32412kb
def rotate(chain, choice, direc):
    rot = direc
    before = chain[choice][2]
    for i in range(choice + 1, 4):
        if before == chain[i][6]:
            break
        before = chain[i][2]
        if rot == -1:
            chain[i].insert(0, chain[i].pop())
        else:
            chain[i].append(chain[i].pop(0))
        rot = [0, -1, 1][rot]

    rot = direc
    before = chain[choice][6]
    for i in range(choice - 1, -1, -1):
        if before == chain[i][2]:
            break
        before = chain[i][6]
        if rot == -1:
            chain[i].insert(0, chain[i].pop())
        else:
            chain[i].append(chain[i].pop(0))
        rot = [0, -1, 1][rot]

    if direc == 1:
        chain[choice].insert(0, chain[choice].pop())
    else:
        chain[choice].append(chain[choice].pop(0))





num = 4
chain = [list(map(int, list(input()))) for _ in range(num)]
command_num = int(input())
for _ in range(command_num):
    choice, direc = map(int, list(input().split()))
    rotate(chain, choice - 1, direc)

print(chain[0][0] + chain[1][0] * 2 + chain[2][0] * 4 + chain[3][0] * 8)


