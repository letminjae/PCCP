# 순서쌍의 개수

def solution(n):
  answer = 0
  for i in range(1,n+1):
    if(n % i == 0): answer += 1
  return answer

print(solution(20))