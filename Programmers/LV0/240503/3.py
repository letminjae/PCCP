# 7의 개수

def solution(array):
  answer = 0
  for num in array:
    answer += list(str(num)).count('7')
  return answer