# 정사각형으로 만들기

def solution(arr):
  answer = []
  row = len(arr)
  col = len(arr[0])
  print(row, col)
  if row > col:
    for i in arr:
      answer.append(i + [0] * (row - col))
  elif row < col:
    for j in range(col - row):
      arr.append([0] * col)
    answer = arr
  else: 
    answer = arr
  return answer

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))