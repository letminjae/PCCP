# 1629 - 곱셈
# 모듈러 거듭제곱

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(A, B):
    if B == 1:
        return A % C
    else:
        temp = power(A, B//2)
        # 짝수
        if B % 2 == 0:
            return (temp * temp) % C
        # 홀수는 한번더 A를 곱한다
        else:
            return (temp * temp * A) % C

print(power(A, B))