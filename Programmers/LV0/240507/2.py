# 직사각형 넓이 구하기

def solution(dots):
  row = []
  col = []
  for s, e in dots:
    row.append(s)
    col.append(e)
  return (max(row) - min(row)) * (max(col) - min(col))