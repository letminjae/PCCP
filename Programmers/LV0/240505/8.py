# 구슬을 나누는 경우의 수

from math import factorial

def solution(balls, share):
    n = factorial(balls)
    m = factorial(share)
    r = factorial(balls - share) * m
    return n / r

print(solution(3, 2))