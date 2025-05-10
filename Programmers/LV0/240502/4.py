# 가까운 수

def solution(array, n):
  arr = []
  array.sort()
  for v in array:
    arr.append(abs(v - n))
  return array[arr.index(min(arr))]