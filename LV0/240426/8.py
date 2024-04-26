# 두 수의 연산값 구하기

def solution(a, b):
  operation1 = int(str(a) + str(b))
  operation2 = 2 * a * b
  if operation1 > operation2 : return operation1
  else : return operation2

print(solution(2, 91))

# max method 를 사용해보자..!