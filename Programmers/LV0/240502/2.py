# A로 B 만들기

def solution(before, after):
  sortedBefore = sorted(before)
  sortedAfter = sorted(after)
  if sortedBefore == sortedAfter:
    return 1
  else: return 0