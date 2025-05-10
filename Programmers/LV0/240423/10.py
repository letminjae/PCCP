# 길이에 따른 연산

def solution(num_list):
  answer = 0
  if len(num_list) >= 11:
    for i in num_list:
      answer += i
  else: 
    answer = 1
    for i in num_list:
       answer *= i
  return answer

print(solution([4, 2, 2, 1]))