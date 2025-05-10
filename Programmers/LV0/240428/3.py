# 외계행성의 나이

def solution(age):
  answer = ''
  for i in str(age):
    answer += chr(ord(i)+49)
  return answer

print(solution(23))