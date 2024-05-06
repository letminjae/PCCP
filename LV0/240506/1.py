# 수열과 구간 쿼리 2

def solution(arr, queries):
  answer = []
  for s, e, k in queries:
    tmp = arr[s:e+1]
    tmp.sort()
    for i in tmp:
      if i > k:
        answer.append(i)
        break
      elif i == tmp[-1]:
        answer.append(-1)
  return answer

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))