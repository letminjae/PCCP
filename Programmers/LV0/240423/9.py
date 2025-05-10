# 원하는 문자열 찾기

def solution(myString, pat):
  lowerString = myString.lower()
  lowerPat = pat.lower()
  if(lowerPat in lowerString): return 1
  else: return 0

print(solution("AbCdEfG","aBc"))