# 2294 - 동전 2

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [100001 for _ in range(K+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[K] == 100001:
    print(-1)
else:
    print(dp[K])