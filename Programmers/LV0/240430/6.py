# 세로 읽기

def solution(my_string, m, c):
    answer = ''
    for i in range(c-1,len(my_string),m):
        answer += my_string[i]
    return answer

print(solution("ihrhbakrfpndopljhygc",4,2))