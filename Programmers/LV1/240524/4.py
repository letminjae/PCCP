# 삼진법 뒤집기

def solution(n):
    answer = ''
    while n >= 1:
        rest = n % 3
        n = n // 3
        answer += str(rest)
    return int(answer, 3)