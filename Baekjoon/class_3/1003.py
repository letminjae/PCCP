# 1003 피보나치 함수

import sys
input = sys.stdin.readline

N = int(input())
    
for _ in range(N):
    number = int(input())
    a, b = 1, 0
    for i in range(number):
        a, b = b, a+b
    print(a, b)