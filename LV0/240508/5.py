# 배열 만들기 2

def solution(l, r):
  answer = []
  for i in range(l,r+1):
    if all(num in ['0', '5'] for num in str(i)):
      answer.append(i)
  if len(answer) == 0:
    return [-1]
  return answer