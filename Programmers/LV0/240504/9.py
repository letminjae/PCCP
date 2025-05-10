# 문자 개수 세기

def solution(my_string):
    answer = [0] * 52
    for string in my_string:
        if string.isupper(): k = 65
        else: k = 71
        answer[ord(string)-k] += 1
    return answer

print(solution("Programmers"))