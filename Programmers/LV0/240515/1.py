# 평행

def solution(dots):
  answer = 0
  dots_idx = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 2, 0, 3]]
  for d1, d2, d3, d4 in dots_idx:
      x1, y1 = dots[d1][0], dots[d1][1]
      x2, y2= dots[d2][0], dots[d2][1]
      x3, y3= dots[d3][0], dots[d3][1]
      x4, y4= dots[d4][0], dots[d4][1]
      if (y1-y2)*(x3-x4) == (y3-y4)*(x1-x2) :
          answer = 1
  return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))