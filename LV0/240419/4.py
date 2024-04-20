def solution(hp):
  X = hp // 5
  Y = hp % 5 // 3
  Z = hp % 5 % 3 // 1
  return X+Y+Z