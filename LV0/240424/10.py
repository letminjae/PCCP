# 첫 번째로 나오는 음수

def solution(num_list):
  for i, number in enumerate(num_list):
    if number < 0:
      return i
  return -1

print(solution([12, 4, 15, 46, 38, -2, 15]))