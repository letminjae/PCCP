# 주사위 게임 2

def solution(a, b, c):
  if a != b != c != a: return a+b+c
  elif a !=b or b !=c or a !=c: return (a + b + c) * (a*a + b*b + c*c)
  elif a == b == c: return (a + b + c) * (a*a + b*b + c*c) * (a**3 + b**3 + c**3)

print(solution(4, 4, 4))