# 9461 파도반 수열

import sys
input = sys.stdin.readline
T = int(input())
arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
  arr.append(arr[i-2]+arr[i-3])

for _ in range(T):
    number = int(input())
    print(arr[number])