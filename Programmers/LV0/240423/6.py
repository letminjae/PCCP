# 배열에서 문자열 대소문자 변환하기

def solution(strArr):
  answer = []
  for i, item in enumerate(strArr, start=1):
    print(i, item)
    if(i % 2 == 0): answer.append(item.upper())
    else: answer.append(item.lower())
  return answer

print(solution(["AAA","BBB","CCC","DDD"]))