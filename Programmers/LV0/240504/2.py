# 커피 심부름

def solution(order):
  answer = 0
  for coffee in order:
    if 'americano' in coffee:
      answer += 4500
    elif 'latte' in coffee:
      answer += 5000
    else:
      answer += 4500
  return answer