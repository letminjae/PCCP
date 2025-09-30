# 2630 색종이 만들기

import sys
input = sys.stdin.readline

N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def divide_square(y, x, n):
    global white, blue
    color = square[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != square[i][j]:
                divide_square(y, x, n // 2)  # 1사분면
                divide_square(y, x + n // 2, n // 2)  # 2사분면
                divide_square(y + n // 2, x, n // 2)  # 3사분면
                divide_square(y + n // 2, x + n // 2, n // 2)  # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1
        
divide_square(0, 0, N)
print(white)
print(blue)