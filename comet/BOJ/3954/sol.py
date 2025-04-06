import sys
sys.stdin = open("input.txt", "r")
#############################################
## 시간복잡도 : 10212ms
## 공간복잡도 : 113832kb
def start():
    memory, len_code, len_input = map(int, input().strip().split())
    program = input().strip()
    string = input().strip()
    arr = [0] * (memory)
    roop = 0
    pointer = 0
    command = 0
    str_cusor = 0
    roop_memory = {}
    did_roop = {}
    stack = []
    result = -1
    for i in range(len_code):
        if program[i] == '[':
            stack.append(i)
            did_roop[i] = 0
        elif program[i] == ']':
            temp = stack.pop()
            roop_memory[temp] = i
            roop_memory[i] = temp
            did_roop[i] = 0
    stack = []
    while roop < 100000000:
        if command == len_code: # 명령어 다 수행하면 종료
            break

        if program[command] == '-':
            arr[pointer] -= 1
            if arr[pointer] < 0:
                arr[pointer] = 255

        elif program[command] == '+':

            arr[pointer] += 1
            if arr[pointer] > 255:
                arr[pointer] = 0
        elif program[command] == '<':
            pointer -= 1
            if pointer < 0:
                pointer = memory - 1
        elif program[command] == '>':
            pointer += 1
            if pointer >= memory:
                pointer = 0
        elif program[command] == '[':
            stack.append([command, 0])

            if not arr[pointer]:
                temp = stack.pop()
                if stack:
                    stack[-1][1] += temp[1]

                command = roop_memory[command]


        elif program[command] == ']':

            if arr[pointer]:
                command = roop_memory[command]
            else:
                temp = stack.pop()
                if stack:
                    stack[-1][1] += temp[1]

        elif program[command] == ',':
            if str_cusor == len_input:
                arr[pointer] = 255
            else:
                arr[pointer] = ord(string[str_cusor])
                str_cusor += 1

        if stack:

            stack[-1][1] += 1
            if stack[-1][1] > 50000000:
                print('Loops', stack[-1][0], roop_memory[stack[-1][0]])
                return
        command += 1
        roop += 1



    print('Terminates')
    return

T = int(input())
for tc in range(1, T+1):
    start()