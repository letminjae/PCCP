# 최빈값 구하기

def solution(array):
    savenum = 0
    answer = 0
    for i in set(array):
        if array.count(i) > savenum:
            savenum = array.count(i)
            answer = i
        elif array.count(i) == savenum:
            answer = -1
    return answer