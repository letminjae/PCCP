# 2447 별 찍기 - 10

import sys
input = sys.stdin.readline

def draw_stars(n):
    if n == 1:
        return ['*']
    
    stars = draw_stars(n//3)
    arr = []

    for star in stars:
        arr.append(star * 3)
    for star in stars:
        arr.append(star + ' '*(n//3) + star)
    for star in stars:
        arr.append(star * 3)
    
    return arr

N = int(input())
print('\n'.join(draw_stars(N)))