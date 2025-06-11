# 10870 피보나치수 5

import sys
input = sys.stdin.readline

N = int(input())

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo(n-2) + fibo(n-1)

print(fibo(N+1))