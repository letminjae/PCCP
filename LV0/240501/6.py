# 배열 만들기 5

def solution(intStrs, k, s, l):
  answer = []
  for num in intStrs:
    if int(num[s:s+l]) > k: answer.append(int(num[s:s+l]))
  return answer

print(solution(["0123456789","9876543210","9999999999999"],50000,5,5))