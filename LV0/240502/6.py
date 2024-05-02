# 배열의 길이를 2의 거듭제곱으로 만들기

def solution(arr):
  answer = 0
  length = len(arr)
  while length > 1:
    length = length / 2
    answer += 1
  return arr + [0] * (2 ** answer - int(len(arr)))