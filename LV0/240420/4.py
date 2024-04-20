#최댓값 만들기

def solution(numbers):
  numbers.sort()
  return numbers[-1] * numbers[-2]

print(solution([0,31,24,10,1,9]))