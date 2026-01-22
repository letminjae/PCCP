# 11054 - 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp_increase = [1]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)

dp_decrease = [1]*N

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

dp = [0]*N
for i in range(N):
    dp[i] = dp_increase[i] + dp_decrease[i] -1 

print(max(dp))