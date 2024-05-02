# 한 번만 등장한 문자

def solution(s):
  answer = []
  setStr = set(s)
  for str in setStr:
    if s.count(str) == 1:
      answer.append(str)
  answer.sort()
  return ''.join(answer)