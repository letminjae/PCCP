# 조건에 맞게 수열 변환하기 1

def solution(arr):
  answer = []
  for i in arr:
    if i >= 50 and i % 2 == 0:
        answer.append(i//2)
    elif i < 50 and i % 2 != 0:
        answer.append(i*2)
    else: answer.append(i)
  return answer

print(solution())