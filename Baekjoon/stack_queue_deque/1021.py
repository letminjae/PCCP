# 1021 회전하는 큐

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()

for i in range(N):
    q.append(i+1)

count = 0
i = 0

while i < M:
    if arr[i] == q[0]:
        q.popleft()
        i += 1
    else:
        mid = int(len(q)/2)
        if q.index(arr[i]) <= mid:
            number = q.popleft()
            q.append(number)
            count += 1
        else:
            number = q.pop()
            q.appendleft(number)
            count += 1

print(count)