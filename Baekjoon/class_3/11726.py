# 11726 2*N타일링

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])