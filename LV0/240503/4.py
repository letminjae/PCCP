# 문자열 묶기

def solution(strArr):
  length = []
  for str in strArr:
    length.append(len(str))

  answer = []
  for i in set(length):
    answer.append(length.count(i))
  return max(answer)