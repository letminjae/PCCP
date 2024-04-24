# 할 일 목록
def solution(todo_list, finished):
  answer = []
  for i, bool in enumerate(finished):
    if bool == False:
      answer.append(todo_list[i])
  return answer

print(solution())