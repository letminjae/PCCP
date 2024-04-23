# x 사이의 개수

def solution(myString):
    answer = []
    for i in myString.split('x'):
      answer.append(len(i))
    return answer

print(solution("oxooxoxxox"))