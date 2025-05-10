# 순서 바꾸기

# def solution(num_list, n):
#   answer = []
#   for i in range(n, len(num_list)):
#     answer.append(num_list[i])
#   for i in range(n):
#     answer.append(num_list[i])
#   return answer

def solution(num_list, n):
  return num_list[n:] + num_list[:n]

print(solution([5, 2, 1, 7, 5],3))