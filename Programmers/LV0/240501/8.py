# 진료 순서 정하기

def solution(emergency):
  answer = []
  seq = sorted(emergency, reverse=True)
  for num in emergency:
    answer.append(seq.index(num)+1)
  return answer

print(solution([3, 76, 24]))