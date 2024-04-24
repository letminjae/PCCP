# 홀수 vs 짝수
def solution(num_list):
  odd = 0
  even = 0
  for i, num in enumerate(num_list):
    if i % 2 == 0: even += num
    else: odd += num
  if even > odd: return even
  else: return odd

print(solution())