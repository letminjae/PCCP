# 삼총사

def solution(number):
  answer = 0
  length = len(number)
  for i in range(length):
    for j in range(i+1, length):
      for k in range(j+1, length):
        if number[i] + number[j] + number[k] == 0:
          answer += 1
  return answer

print(solution([-2, 3, 0, 2, -5]))