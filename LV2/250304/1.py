# 가장 큰 수

def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True) # 문자열 3번 반복 시, 비교할 때 자리수가 맞춰져 크기비교가 가능
    return str(int(''.join(numbers)))