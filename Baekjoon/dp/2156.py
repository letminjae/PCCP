# 2156 포도주 시식

import sys
input = sys.stdin.readline

N = int(input())

arr = [0]
for _ in range(N):
    arr.append(int(input()))
dp = [0 for _ in range(N+1)]

dp[0] = 0
dp[1] = arr[1]

if N > 1:
    dp[2] = arr[1] + arr[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3])

print(dp[N])