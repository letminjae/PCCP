# 종이 자르기

def solution(M, N):
  answer = M*N
  if answer == 1:
    answer = 0
  else:
    answer = answer -1
  return answer
