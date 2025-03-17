# PCCP 기출 2번 문제 - 퍼즐게임 챌린지

def check(level, diffs, times, limit):
  total_time = 0
  prev_time = 0
  
  for i in range(len(diffs)):
    diff = diffs[i]
    current_time = times[i]
    
    if diff <= level:
      total_time += current_time
    else:
      fail = diff - level # 틀린 횟수
      total_time += fail * (current_time + prev_time) + current_time
      
    prev_time = current_time
    
    # 제한 시간 초과 시, False
    if total_time > limit:
      return False
    
  return True

# 이분 탐색
def solution(diffs, times, limit):
  left, right = 1, max(diffs)
  
  while left < right:
    mid = (left + right) // 2
    if check(mid, diffs, times, limit):
      right = mid
    else:
      left = mid + 1
  
  return left

solution([1, 5, 3],[2, 4, 7],30) # 3