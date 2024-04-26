# 원소들의 곱과 합

def solution(num_list):
  multiply = 1
  sum = 0
  for num in num_list:
    multiply *= num
    sum += num
  if multiply < sum ** 2 : return 1
  else: return 0