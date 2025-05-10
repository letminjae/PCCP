# 이어 붙인 수

def solution(num_list):
  odd = ''
  even = ''
  for num in num_list:
    if(num % 2 == 0):
      even += str(num)
    else:
      odd += str(num)
  return int(odd) + int(even)