# 문자열 뒤집기

def solution(my_string, s, e):
  reversed_string = ''
  for i in range(e, s-1, -1):
    reversed_string += my_string[i]
  return my_string.replace(my_string[s:e+1], reversed_string)

print(solution("Progra21Sremm3",6,12))