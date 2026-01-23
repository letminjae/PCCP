# 11052 - 카드 구매하기 (실버1)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] + arr

for i in range(1,N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
    
print(max(dp))