# 124 나라의 숫자

def solution(n):
    number = ["1", "2", "4"]
    answer = ""
    
    while n > 0:
        n -= 1
        answer += number[n % 3]
        n //= 3

    return ''.join(reversed(answer))