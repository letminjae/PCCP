# 롤케이크 자르기

def solution(topping):
  answer = 0
  older_brother = {}
  younger_brother = {}

  for t in topping:
    if t in older_brother:
      older_brother[t] += 1
    else:
      older_brother[t] = 1

  for t in topping:
    if len(older_brother) == len(younger_brother):
      answer += 1
    if t not in younger_brother:
      younger_brother[t] = 1
    older_brother[t] -= 1
    if older_brother[t] == 0:
      del older_brother[t]
  return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])