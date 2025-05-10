# 피자 나눠먹기 2

def solution(n):
  pizza = 6
  while pizza % n != 0:
    pizza += 6
  return pizza // 6

print(solution(10))