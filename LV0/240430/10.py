# 중복된 문자 제거

def solution(my_string):
  answer = []
  for i in my_string:
    if i not in answer:
      answer.append(i)
  return "".join(answer)

print(solution("people"))