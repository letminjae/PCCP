#세균 증식

def solution(n, t):
    for i in range(1 , t+1):
      n = n * 2
    return n

print(solution(7, 15))

# 제곱을 쓴다면
def solution2(n,t):
   return n*(2**t)

print(solution2(7,15))