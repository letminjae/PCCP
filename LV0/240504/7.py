# 잘라서 배열로 저장하기

def solution(my_str, n):
  answer = []
  for i in range(0, len(my_str), n):
    answer.append(my_str[i:i+n])
  return answer