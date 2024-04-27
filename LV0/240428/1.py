# 조건에 맞게 수열 변환하기

def solution(arr, k):
  answer = []
  for i in arr:
    if k % 2 != 0:
      answer.append(i*k)
    else: answer.append(i+k)
  return answer

print(solution([1, 2, 3, 100, 99, 98],3))