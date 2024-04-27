# 부분 문자열인지 확인하기

def solution(my_string, target):
  return int(target in my_string)

print(solution("banana", "ana"))