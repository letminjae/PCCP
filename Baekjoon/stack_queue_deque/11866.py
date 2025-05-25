# 11866 요새푸스 문제 0

from collections import deque

N, K = map(int, input().split())

deque = deque([i for i in range(1, N+1)])

answer = []

while len(deque) != 0:
  for _ in range(K-1):
    deque.append(deque.popleft())
  answer.append(str(deque.popleft()))
  
print('<' + ', '.join(answer) + '>')