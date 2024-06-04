# 햄버거 만들기

# 시간초과
# def solution(ingredient):
#     answer = 0
#     ingredient = "".join([str(i) for i in ingredient])
#     burger = "1231"
#     while ingredient.find(burger) != -1:
#         answer += 1
#         ingredient = ingredient.replace(burger, "", 1)
#     return answer

# 시간초과 개선 - 스택 사용
def solution(ingredient):
    answer = 0
    stack = []
   
    for i in ingredient:
        stack.append(i)
        if stack[-4:]==[1,2,3,1]:
            answer+=1
            for _ in range(4):
                stack.pop()

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))