# 1로 만들기

def solution(num_list):
  answer = 0
  for num in num_list:
    count = 0
    while num != 1:
      count += 1
      if num % 2 == 0:
        num = num / 2
      else:
        num = (num - 1) / 2
    answer += count
  return answer