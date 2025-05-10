# 숫자 찾기

def solution(numbers, k):
  numbers = str(numbers)
  k = str(k)
  for i, number in enumerate(numbers, start=1):
    if number == k: return i
  return -1

print(solution(29183,1))