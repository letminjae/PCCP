# k의 개수

def solution(x, y, k):
  answer = list()
  for i in range(x, y+1):
    answer += list(str(i))
  return answer.count(str(k))