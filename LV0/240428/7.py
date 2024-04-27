# 문자열 정렬하기

def solution(my_string):
    answer = []
    for str in my_string:
      answer.append(str.lower())
    answer.sort()
    return ''.join(answer)

print(solution("Bcad"))