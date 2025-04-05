import sys
sys.stdin = open("input.txt", 'r')
"""
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
"""

width, height= 100, 100
white_board = [[0] * width for _ in range(height)]

result = 0
count = int(input())
for _ in range(count):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if white_board[i][j] == 1: continue
            white_board[i][j] = 1
            result+=1

print(result)


#
# for i in range(width):
#     for j in range(height):
#         if white_board[i][j] != 0:
#             result += 1
#
# print(result)




