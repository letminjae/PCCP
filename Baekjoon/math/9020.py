# 9020 - 골드바흐의 추측 (실버 2)

import sys
input = sys.stdin.readline
import math

T = int(input())

def is_prime_number(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
            
    return True

for _ in range(T):
    target = int(input())
    
    A = target // 2
    B = target // 2

    for _ in range(target // 2):
        if is_prime_number(A) and is_prime_number(B):
            print(A, B)
            break
        else:
            A -= 1
            B += 1