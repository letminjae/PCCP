# 공 던지기

def solution(numbers, k):
  answer = 0
  numbers = numbers * k
  answer = numbers[2*(k-1)]
  return answer

print(solution([1, 2, 3, 4],2))