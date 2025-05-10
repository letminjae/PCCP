# 그림 확대

def solution(picture, k):
  answer = []
  for row in picture:
    per = ''
    for pixel in row:
      per += pixel * k
    for _ in range(k):
      answer.append(per)
  return answer

print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."],2))