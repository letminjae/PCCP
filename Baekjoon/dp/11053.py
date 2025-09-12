# 11053 - 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N # dp[i] = arr[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))