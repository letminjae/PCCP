# 1932 - 정수삼각형

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)-2, -1, -1):
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])

print(arr[0][0])