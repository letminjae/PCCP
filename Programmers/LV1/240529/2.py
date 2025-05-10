# 콜라 문제

def solution(a, b, n):
    coke = 0
    while n >= a:
        bottle = n % a
        n = (n // a) * b
        coke += n
        n += bottle
    return coke

print(solution(3, 1, 20))