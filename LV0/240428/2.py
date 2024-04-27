# 가까운 1 찾기

def solution(arr, idx):
  for i, num in enumerate(arr):
    if i >= idx and num == 1: return i
  else: return -1

print(solution([0, 0, 0, 0], 1))