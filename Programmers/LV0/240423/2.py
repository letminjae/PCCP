# 공백으로 구분하기 1

def solution(my_string):
    answer = []
    for i in my_string.split(' '):
      answer.append(i)
    return answer

print(solution("i love you"))