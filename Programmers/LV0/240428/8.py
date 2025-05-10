# 특이한 이차원 배열 1

def solution(n):
  answer = []
  for i in range(n):
    arr = []
    for j in range(n):
      if i == j: arr.append(1)
      else: arr.append(0)
    answer.append(arr)
  return answer

print(solution(3))