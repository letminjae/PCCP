# 나무 자르기
# pypy3로 제출

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))
start, end = 1, max(height)

while start <= end:
    mid = (start+end) // 2
    
    sum = 0
    for i in height:
        if i >= mid:
            sum += i - mid
    
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)