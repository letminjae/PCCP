# 세 개의 구분자

def solution(myStr):
  answer = []
  seperate = ["a", "b", "c"]
  for sep in seperate:
    myStr = myStr.replace(sep," ")
    answer = myStr.strip().split()
  if answer == [] : answer.append("EMPTY")
  return answer