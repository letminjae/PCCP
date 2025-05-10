# 정수 제곱근 판별

def solution(n):
    if n ** (1/2) % 1 == 0:
        return int((n**(1/2)+1) ** 2)
    else:
        return -1