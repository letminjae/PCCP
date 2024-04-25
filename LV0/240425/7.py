# 부분 문자열 이어 붙어 문자열 만들기

def solution(my_strings, parts):
  answer = ''
  for i, string in enumerate(my_strings):
    answer += string[parts[i][0]:parts[i][1]+1]
  return answer

print(solution())