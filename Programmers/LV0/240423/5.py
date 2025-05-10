# A 강조하기

def solution(myString):
  answer = ''
  for i in myString:
    if(i.isupper() == True):
      answer += i.lower()
    else: answer += i
  return answer.replace("a", "a".upper())

print(solution("PrOgRaMmErS"))