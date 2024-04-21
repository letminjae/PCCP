#제곱수 판별하기
import math

def solution(n):
    if (n ** 0.5).is_integer(): return 1 
    else: return 2

print(solution(141234))