# 조이스틱

def solution(name):
  count = 0
  # 무난히 오른쪽으로 이동 시, len(name) - 1 만큼 이동
  move = len(name) - 1

  for i in range(len(name)):
    # 왼쪽, 오른쪽 : 타겟-A 또는 Z-타겟+1
    count += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
   
    # 위, 아래
    # j값 구하기 : A가 나올 때까지 인덱스 이동
    j = i+1
    while j < len(name) and name[j] == 'A':
      j += 1
    move = min([move, 2*i+(len(name)-j), i+2*(len(name)-j)])
 
  return count+move