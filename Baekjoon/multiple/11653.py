# 11653 소인수분해

N = int(input())

number = 2
answer = []

while number * number <= N:
  while N % number == 0:
    answer.append(number)
    N //= number
  number += 1
  
if N > 1:
  answer.append(N)

for num in answer:
  print(num)