# 17626 Four Squares - PyPy3로 통과

import sys
input = sys.stdin.readline

N = int(input())

dp = [float('inf')] * (N+1)
dp[0] = 0

for number in range(1, N+1):
    sqrt = 1
    while sqrt*sqrt <= number:
        dp[number] = min(dp[number], dp[number-(sqrt*sqrt)]+1)
        sqrt += 1

print(dp[N])