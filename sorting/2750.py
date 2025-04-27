# 2750 - 수 정렬하기

N = int(input())

answer = sorted([int(input()) for _ in range(N)])

for num in answer:
  print(num)