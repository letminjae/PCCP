# 1463 1로 만들기

import sys
input = sys.stdin.readline

X = int(input())

dp = [0] * 10000001

for i in range(2, X+1):
    # 3과 2로 나눠지지 않으면 1 빼기
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[X])