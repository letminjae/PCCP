# Jadencase 문자열 만들기

def solution(s):
    answer = ''
    s = s.lower()
    for i in range(len(s)):
        if i == 0 and s[i].isalpha:
            answer += s[i].upper()
        elif s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer

print(solution("for the last week"))