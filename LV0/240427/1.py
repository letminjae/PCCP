# 홀짝 구분하기

def solution(n):
  if n % 2 == 0: return f"{n} is even"
  else: return f"{n} is odd"

print(solution(100))