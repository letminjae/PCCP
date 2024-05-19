# 두 정수 사이의 합

def solution(a,b):
  return int((a+b) * (abs(b-a)+1)/2)

print(solution(5,3))