# 컨트롤 제트

def solution(s):
    answer = 0
    s_list = list(s.split(" "))
    for i in range(len(s_list)):
        if s_list[i] == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(s_list[i])
    return answer

print(solution("1 2 Z 3"))