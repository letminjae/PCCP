# 등수 매기기

def solution(score):
  rank = []
  average = [sum(i)/2 for i in score]
  s_average = sorted(average, reverse=True)
  for i in average:
    rank.append(s_average.index(i)+1)
  return rank