# 삼각형의 완성조건 (2)

def solution(sides):
  count = 0
  sides.sort()
  for i in range(sides[1]+1, sides[0]+sides[1]):
    count += 1
  for j in range(sides[1], sides[1]-sides[0], -1):
    count += 1
  return count
  

print(solution([11,7]))