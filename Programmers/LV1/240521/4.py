# 문자열 나누기

def solution(s):
    answer = 0
    first_cnt = 0
    other_cnt = 0
   
    for i in s:
        if first_cnt == other_cnt:
            answer += 1
            tmp = i
           
        if tmp == i:
            first_cnt += 1
        else:
            other_cnt += 1

    return answer