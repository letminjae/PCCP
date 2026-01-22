# 11055 - 가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    dp[i] = arr[i]

for i in range(N):
    for j in range(i):
        # 수열이고, 이전값이 작은것들만 arr[i]에 더하기
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))