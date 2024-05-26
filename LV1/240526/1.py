# 크기가 작은 부분 문자열

def solution(t, p):
    answer = 0
    p_length = len(p)
    t_length = len(t)
    for i in range(0, t_length+1 - p_length):
        if int(t[i:i+p_length]) <= int(p):
          answer += 1
    return answer

print(solution("3141592","271"))