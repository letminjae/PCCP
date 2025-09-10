# 프로그래머스 LV3 - 가장 긴 펠린드롬

def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]: # 팰린드롬인지 확인
                answer = max(answer, len(s[i:j]))

    return answer

solution("abcdcba")
solution("abacde")