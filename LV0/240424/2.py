# n보다 커질 때까지 더하기
def solution(numbers, n):
  answer = 0
  for i in numbers:
    if answer <= n :
      answer += i
  return answer

print(solution())