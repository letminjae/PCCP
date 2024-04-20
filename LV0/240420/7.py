#숨어있는 숫자의 덧셈(1)

def solution(my_string):
    answer = 0
    for i in my_string:
      if(i.isdigit() == True): answer += int(i)
    return answer

print(solution("aAb1B2cC34oOp"))