# 9465 - 스티커

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input()) # 열의 개수
    sticker = []
    for i in range(2):
        sticker.append(list(map(int, input().split())))
    
    if N == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    
    dp = [[0] * 2 for _ in range(N+1)]
    dp[1] = [sticker[0][0], sticker[1][0]]

    for i in range(2, N+1):
        dp[i][0] = sticker[0][i-1] + max(dp[i-1][1], dp[i-2][1])
        dp[i][1] = sticker[1][i-1] + max(dp[i-1][0], dp[i-2][0])

    print(max(dp[N][0], dp[N][1]))