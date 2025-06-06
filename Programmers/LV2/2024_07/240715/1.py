# 뒤에 있는 큰 수 찾기

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            answer[idx] = num
        stack.append(i)

    return answer