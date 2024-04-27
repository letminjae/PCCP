# 문자열 잘라서 정렬하기

def solution(myString):
    answer = []
    str = myString.split('x')
    print(str)
    for i in str:
      if i != "" : answer.append(i)
    answer.sort()
    return answer

print(solution("axbxcxdx"))