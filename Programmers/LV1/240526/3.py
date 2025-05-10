# 이상한 문자 만들기

def solution(s):
  answer = ''
  word = s.split(' ')
  for i in range(len(word)):
    for j in range(len(word[i])):
      if (j % 2) == 0:
        answer += word[i][j].upper()
      else:
        answer += word[i][j].lower()
    if i < len(word) - 1:
      answer += ' '
  return answer

print(solution("try hello world"))