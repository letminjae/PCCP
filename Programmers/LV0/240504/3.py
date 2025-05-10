# 조건에 맞게 수열 변환하기 2

def solution(arr):
  answer = 0
  prev = arr
  while True:
    current = []
    for i in prev:
      if i >= 50 and i % 2 == 0:
        i = i // 2
      elif i < 50 and i % 2 == 1:
        i = i * 2 + 1
      current.append(i)
    if prev == current:
      break
    else:
      prev = current
      answer += 1
  return answer