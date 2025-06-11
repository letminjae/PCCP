# 27433 팩토리얼2

import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(N))