# 이진 변환 반복하기

def solution(s):
  cnt = 0
  loop = 0
  while int(s) > 1:
    loop += 1
    cnt += s.count('0')
    s = s.replace('0','')
    s = bin(len(s))[2:]
  return [loop, cnt]

print(solution("110010101001"))