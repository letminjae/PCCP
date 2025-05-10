# 문자열 정수의 합

def solution(num_str):
  answer = 0
  for i in num_str:
    answer += int(i)
  return answer