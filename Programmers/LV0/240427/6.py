# 부분 문자열

def solution(str1, str2):
    if str1 in str2: return 1
    else: return 0

print(solution("abc", "aabcc"))