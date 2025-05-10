# 팩토리얼

def solution(n):
    answer = 0
    for i in range(10+1):
        if(n >= getFactorial(i)):
            answer = i
            continue
        else:
            break
    return answer

def getFactorial(num):
    if num > 1 :
      return num*getFactorial(num-1)
    return num

print(solution(7))