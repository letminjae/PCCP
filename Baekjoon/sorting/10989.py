# 10989 수 정렬하기 3
# 계수정렬 사용으로 메모리 줄이기

import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * 10001

for _ in range(N):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)