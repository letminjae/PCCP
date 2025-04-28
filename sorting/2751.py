# 2751 수 정렬하기 2

import sys # 시간초과로 readline 사용
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

for num in sorted(arr):
    print(num)