# 2의 영역

def solution(arr):
  index = []
  for i in range(len(arr)):
    if arr[i] == 2:
      index.append(i)
  if len(index) == 0:
    return [-1]
  else:
    return arr[min(index):max(index)+1]