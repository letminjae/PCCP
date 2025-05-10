# 문자열 내 p와 y의 갯수

def solution(s):
    p = 0
    y = 0
    for char in s:
        if char.lower() == "p":
            p += 1
        if char.lower() == "y":
            y += 1
    return True if p == y else False