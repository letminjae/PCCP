# 10773 제로

import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    number = int(input())
    if number == 0:
        arr.pop()
    else:
        arr.append(number)

print(0 if len(arr) == 0 else sum(arr))