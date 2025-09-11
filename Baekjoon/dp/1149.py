# 1149 - RGB 거리

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = arr[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0] # 빨강 = 이전빨강값 + (이전노랑 vs 이전파랑 중 최솟값)
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1] # 노랑 = 이전노랑값 + (이전빨강 vs 이전파랑 중 최솟값)
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2] # 파랑 = 이전빨강값 + (이전빨강 vs 이전노랑 중 최솟값)

print(min(dp[-1]))