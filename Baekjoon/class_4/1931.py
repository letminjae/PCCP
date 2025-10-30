# 1931 회의실 배정

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x:(x[1],x[0]))

time = 0
answer = 0
for meeting in arr:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print(answer)