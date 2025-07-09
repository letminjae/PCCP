# 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

numbers = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i] + numbers[i]

for _ in range(M):
    i, j = map(int, input().split())
    result = dp[j] - dp[i-1]
    print(result)