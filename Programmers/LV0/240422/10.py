# 문자열 바꿔서 찾기

def solution(myString, pat):
    Change_Char = ''
    for char in myString:
        if char == 'A' : Change_Char += 'B'
        else: Change_Char += 'A'
    if pat in Change_Char : return 1
    else : return 0

print(solution("ABBAA","AABB"))