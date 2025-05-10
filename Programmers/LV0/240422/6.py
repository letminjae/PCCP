# 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
  for i, number in enumerate(arr):
    if len(arr) % 2 == 0:
      if i % 2 == 1 :
        arr[i] += n
    else :
      if i % 2 == 0 :
        arr[i] += n
  return arr