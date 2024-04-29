# l로 만들기

def solution(myString):
  answer = ''
  for str in myString:
    if ord(str) < 108:
      str = 'l'
    answer += str  
  return answer