# 올바른 괄호

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
    return True if len(stack) == 0 else False

print(solution("(()("))