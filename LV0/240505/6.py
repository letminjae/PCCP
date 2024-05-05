# 왼쪽 오른쪽

def solution(str_list):
  for i in range(len(str_list)):
    if str_list[i] == 'l':
      return str_list[:i]
    elif str_list[i] == 'r':
      return str_list[i+1:]
  return []

print(solution(["a", "b", "l", "r", "y", "z"]))