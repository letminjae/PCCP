# OX 퀴즈

def solution(quiz):
  result = []
  for i in quiz:
    exp = i.split(' = ')[0]
    answer = i.split(' = ')[1]
    if eval(exp) == int(answer):
      result.append('O')
    else:
      result.append('X')
  return result