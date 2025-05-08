# 14425 문자열 집합

from collections import Counter

N, M = map(int, input().split())

count = Counter([input() for _ in range(N)])
target = [input() for _ in range(M)]

answer = 0

for tar in target:
    if count[tar] == 1:
        answer += 1

print(answer)