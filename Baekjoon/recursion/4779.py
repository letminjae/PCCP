# 4779 칸토어 집합

import sys
input = sys.stdin.readline

def cantore(start, n):
  if n == 1:
    return
  for i in range(start + n//3, start +(n//3)*2): # 가운데 문자열을 공백으로
    result[i] = ' '
  cantore(start, n//3) # 왼쪽 자르기
  cantore(start + n//3 * 2, n//3) # 오른쪽 자르기
    
while True:
  try:
    N = int(input())
    result = ['-'] * (3**N)
    cantore(0, 3**N)
    print(''.join(result))
  except:
    break