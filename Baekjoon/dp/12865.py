# 12865 - 평범한 배낭
# 냅색 알고리즘

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

things = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    things.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])