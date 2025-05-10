# 괄호 회전하기

def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == "[" and s[i] == "]": stack.pop()
                elif stack[-1] == "{" and s[i] == "}": stack.pop()
                elif stack[-1] == "(" and s[i] == ")": stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
        # 맨앞의 글자를 뒤로 옮긴다
        s.append(s.pop(0))
    return answer

print(solution("[](){}"))