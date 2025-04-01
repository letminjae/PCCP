# 소수 찾기

from itertools import permutations

# 에라스토테네스의 체
def prime_check(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    per = []
    
    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))
    
    int_per = [int(''.join(tup)) for tup in per]

    for num in int_per:
        if prime_check(num):
            answer.append(num)

    return len(set(answer))

solution("17")