# 자연수 뒤집어 배열로 만들기

def solution(n):
    return [int(i) for i in list(str(n)[::-1])]