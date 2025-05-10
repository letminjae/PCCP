# 9를 나눈 나머지

def solution(number):
  answer = 0
  for num in number:
    answer += int(num)
  return answer % 9