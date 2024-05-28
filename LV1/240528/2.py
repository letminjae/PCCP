# 문자열 내 맘대로 정렬하기

def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])