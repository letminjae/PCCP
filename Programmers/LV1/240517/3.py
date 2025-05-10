# 정수 내림차순으로 배치하기

def solution(n):
    answer = [i for i in list(str(n))]
    answer.sort(reverse=True)
    return int(''.join(answer))