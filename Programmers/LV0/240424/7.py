# n번째 원소까지
def solution(num_list, n):
  answer = []
  for i in range(0, n):
    answer.append(num_list[i])
  return answer

print(solution())