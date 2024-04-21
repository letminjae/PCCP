#자릿수 더하기

def solution(n):
    answer = 0
    arr = []
    for i in str(n):
      arr.append(int(i))
    for i in arr:
       answer += i
    return answer

print(solution(1234))

# 좀 더 깔끔
def solution2(n):
   n = str(n)
   answer = 0
   for i in n:
     answer += int(i)
   return answer