# 예산

def solution(d, budget):
  answer = 0
  sum = 0
  d.sort()

  for i in range(len(d)):
    answer += 1
    sum += d[i]

    if sum > budget:
      answer -= 1

  return answer

print(solution([1,3,2,5,4],9))