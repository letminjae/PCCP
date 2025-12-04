# 14501 퇴사

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + arr[i][0] > N: # 상담일이 퇴사일을 넘기면 상담 X
        dp[i] = dp[i+1]
    else: # i일에 상담하는 것과 안하는 것 중 큰 것 선택
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

print(dp[0])