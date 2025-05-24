# 2164 카드 2

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

deque = deque([i for i in range(1, N+1)])

while len(deque) > 1:
  deque.popleft()
  second = deque.popleft()
  deque.append(second)
  
print(deque[0])